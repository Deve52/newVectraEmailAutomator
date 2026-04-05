from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import EmailSchedule, EmailTemplate, Group
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

@csrf_exempt
@require_http_methods(["POST"])
def create_schedule(request):
    try:
        data = json.loads(request.body)

        # Basic validation and object retrieval
        user = User.objects.get(id=data.get('user_id'))
        template = EmailTemplate.objects.get(id=data.get('template_id'))
        group = Group.objects.get(id=data.get('group_id'))

        schedule_data = {
            'user': user,
            'template': template,
            'group': group,
            'schedule_type': data.get('schedule_type'),
            'is_active': data.get('is_active', True)
        }

        # Handle optional fields carefully
        run_once_datetime_str = data.get('run_once_datetime')
        if run_once_datetime_str:
            naive_datetime = datetime.fromisoformat(run_once_datetime_str)
            schedule_data['run_once_datetime'] = timezone.make_aware(naive_datetime)

        if data.get('time'):
            schedule_data['time'] = data.get('time')
        
        if data.get('days_of_week'):
            schedule_data['days_of_week'] = data.get('days_of_week')
        
        if data.get('day_of_month'):
            schedule_data['day_of_month'] = data.get('day_of_month')

        if data.get('yearly_date'):
            schedule_data['yearly_date'] = data.get('yearly_date')

        schedule = EmailSchedule.objects.create(**schedule_data)
        return JsonResponse({'status': 'success', 'schedule_id': schedule.id}, status=201)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def modify_schedule(request, schedule_id):
    try:
        data = json.loads(request.body)
        schedule = EmailSchedule.objects.get(id=schedule_id)

        # Update fields
        schedule.template_id = data.get('template_id', schedule.template_id)
        schedule.group_id = data.get('group_id', schedule.group_id)
        schedule.schedule_type = data.get('schedule_type', schedule.schedule_type)
        
        run_once_datetime_str = data.get('run_once_datetime')
        if run_once_datetime_str:
            naive_datetime = datetime.fromisoformat(run_once_datetime_str)
            schedule.run_once_datetime = timezone.make_aware(naive_datetime)
        else:
            schedule.run_once_datetime = None

        schedule.time = data.get('time') if data.get('time') else None
        schedule.days_of_week = data.get('days_of_week') if data.get('days_of_week') else None
        schedule.day_of_month = data.get('day_of_month') if data.get('day_of_month') else None
        schedule.yearly_date = data.get('yearly_date') if data.get('yearly_date') else None
        schedule.is_active = data.get('is_active', schedule.is_active)
        
        schedule.save()
        return JsonResponse({'status': 'success', 'schedule_id': schedule.id})
    except EmailSchedule.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Schedule not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"]) # Should be DELETE, but using POST for simplicity with csrf_exempt
def delete_schedule(request, schedule_id):
    try:
        schedule = EmailSchedule.objects.get(id=schedule_id)
        schedule.delete()
        return JsonResponse({'status': 'success', 'message': 'Schedule deleted'})
    except EmailSchedule.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Schedule not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_http_methods(["GET"])
def get_schedules(request, user_id):
    try:
        schedules = EmailSchedule.objects.filter(user_id=user_id)
        data = list(schedules.values(
            'id', 'template__name', 'group__name', 'schedule_type', 
            'run_once_datetime', 'time', 'days_of_week', 'day_of_month', 
            'yearly_date', 'is_active', 'created_at'
        ))
        return JsonResponse({'status': 'success', 'schedules': data})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

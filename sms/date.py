from multiprocessing import context
from django.forms import DateTimeInput

class BootstrapDateTimePickerInput(DateTimeInput):
    template_name: 'date/reg.html'
    
    def get_context(self, name, value, attrs):
        datetimepicker_id='datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs=dict()
            attrs['data_target']='#{id}'.format(id=datetimepicker_id)
            attrs['class']='form_control datetimepicker_input'
            context=super().get_context(name,value, attrs)
            context['date']['datetimepicker_id']=datetimepicker_id
        return context
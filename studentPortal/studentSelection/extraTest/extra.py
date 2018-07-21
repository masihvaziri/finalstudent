from django.db.models import FileField
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.forms import forms


class ContentTypeRestrictedFileField(FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size_kb", []) * 1024

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('لطفا حجم عکس ارسالی را به زیر  %s.  کاهش دهید . حجم فایل ارسالی شما : %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_(' فرمت عکس مجاز نمی باشد .'))
        except AttributeError:
            pass

        return data

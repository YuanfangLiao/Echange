import xadmin
from xadmin.layout import Main, Fieldset, Row, Side
from xadmin.plugins.auth import UserAdmin
from django.utils.translation import ugettext as _

from myuser.models import MyUser


class MyUserAdminx(UserAdmin):
    # change_user_password_template = None
    list_display = ('id', 'username', 'phone', 'address', 'level', 'credit', 'is_staff',)
    change_user_password_template = None
    exclude = ('groups', 'user_permissions', 'first_name', 'last_name', 'picture',)

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('level', 'credit'),
                             Row('sex', 'email'),
                             Row('phone', ),
                             'address',
                             'signature',
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


xadmin.site.unregister(MyUser)
xadmin.site.register(MyUser, MyUserAdminx)

from django.urls import include, path

urlpatterns = [
    path("auth/", include("nephr_api.api_urls.auth.urls")),
    path("asset/", include("nephr_api.api_urls.asset.urls")),
    path("base/", include("nephr_api.api_urls.base.urls")),
    path("employee/", include("nephr_api.api_urls.employee.urls")),
    path("notifications/", include("nephr_api.api_urls.notifications.urls")),
    path("payroll/", include("nephr_api.api_urls.payroll.urls")),
    path("attendance/", include("nephr_api.api_urls.attendance.urls")),
    path("leave/", include("nephr_api.api_urls.leave.urls")),
]

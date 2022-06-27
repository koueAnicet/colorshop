from SiteWeb.models import Site

def global_Site_info(request):

    site = Site.objects.first()
    return {
        "site_info": site,
    }   
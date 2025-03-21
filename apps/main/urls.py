from django.urls import path

# Views
from . import views

# Routes
urlpatterns = [
    path("", views.home, name="home"),
    path("feedback/", views.survey, name="survey"),
    path("exhibit/", views.exhibit, name="exhibit"),
    path("register/", views.registerAttendance, name="registerAttendance"),
    # PAGES
    path("exhibit/bataanprojects/", views.bataanProjects, name="bataanProjects"),
    path("exhibit/tarlacprojects/", views.tarlacProjects, name="tarlacProjects"),
    path("exhibit/bulacanprojects/", views.bulacanProjects, name="bulacanProjects"),
    path("exhibit/pampangaprojects/", views.pampangaProjects, name="pampangaProjects"),
    path("exhibit/otherprojects/", views.otherProjects, name="otherProjects"),
    path("exhibit/kaayusan/", views.kaayusan, name="kaayusan"),
    path("exhibit/kalusugan/", views.kalusugan, name="kalusugan"),
    path("exhibit/kabuhayan/", views.cest, name="cest"),
    path("policy/", views.policy, name="policy"),
    path("guide/", views.guide, name="guide"),
    # EQUIPMENTS
    path(
        "exhibit/amrel/filamentwinder",
        views.filamentWinder,
        name="filamentWinder",
    ),
    path(
        "exhibit/amrel/microwavefurnace",
        views.microwaveFurnace,
        name="microwaveFurnace",
    ),
    path("exhibit/amrel/creatorpro", views.creatorPro, name="creatorPro"),
    path("exhibit/amrel/formlabform2", views.formLab, name="formLab"),
    path("exhibit/amrel/microscope", views.microscope, name="microscope"),
    path(
        "exhibit/amrel/shimadzuagsxseries",
        views.shimadzuAgs,
        name="shimadzuAgs",
    ),
    path("exhibit/amrel/impacttester", views.impactTester, name="impactTester"),
    path(
        "exhibit/amrel/injectionmodelingmachine",
        views.injectionModeling,
        name="injectionModeling",
    ),
    path("exhibit/amrel/uvcuringapparatus", views.uvCuring, name="uvCuring"),
    path("exhibit/amrel/shining3deinscanse", views.shining3d, name="shining3d"),
    path(
        "exhibit/amrel/filamentextruder",
        views.filamentExtruder,
        name="filamentExtruder",
    ),
    path(
        "exhibit/amrel/shimadzurockwelltypehardnesstester",
        views.shimadzuRockwell,
        name="shimadzuRockwell",
    ),
    path("exhibit/amrel/zortraxm200", views.zortrax, name="zortrax"),
    path("exhibit/amrel/viscometer", views.viscometer, name="viscometer"),
    path("exhibit/amrel/ultimaker3extended", views.ultimaker, name="ultimaker"),
    path("exhibit/amrel/sonicbath", views.sonicBath, name="sonicBath"),
    path("exhibit/kinabukasan/amrel", views.amrel, name="amrel"),
    path(
        "exhibit/kinabukasan/automatedguidewaytransit",
        views.automated,
        name="automated",
    ),
    path("exhibit/kinabukasan/designedclassroom", views.adoption, name="adoption"),
    path("exhibit/kinabukasan/ilab", views.innovative, name="innovative"),
    path("exhibit/kinabukasan/foodinnovationcenter", views.food, name="food"),
    path("exhibit/kinabukasan/improvingagricultural", views.agri, name="agri"),
    path("exhibit/kinabukasan/tbi", views.tbi, name="tbi"),
    path("exhibit/kinabukasan/tamarind", views.tamarind, name="tamarind"),
    path("exhibit/kinabukasan/sweetpotato", views.sweet, name="sweet"),
    path("exhibit/kinabukasan/projectmist", views.mist, name="mist"),
    path("exhibit/kinabukasan/foodsafetycontrol", views.safety, name="safety"),
    path(
        "exhibit/kinabukasan/designanddevelopment",
        views.development,
        name="development",
    ),
    path(
        "exhibit/kinabukasan/support",
        views.support,
        name="support",
    ),
    path(
        "exhibit/kinabukasan/support",
        views.support,
        name="support",
    ),
    path(
        "exhibit/kinabukasan/",
        views.kinabukasan,
        name="kinabukasan",
    ),
    path(
        "exhibit/kinabukasan/starbooks",
        views.starbooks,
        name="starbooks",
    ),
    path(
        "exhibit/kinabukasan/far-uvcgate",
        views.far,
        name="far",
    ),
    path(
        "exhibit/kinabukasan/teachingaids",
        views.teach,
        name="teach",
    ),
    # KAAYUSAN
    path("exhibit/kaayusan/duck", views.duck, name="duck"),
    path("exhibit/kaayusan/jauntimeclock", views.clock, name="clock"),
    path("exhibit/kaayusan/swan", views.swan, name="swan"),
    # KALUGUSAN
    path("exhibit/kalugusan/feedingprogram", views.feeding, name="feeding"),
    path("exhibit/kalugusan/rxbox", views.rxbox, name="rxbox"),
    path("exhibit/kalugusan/clhrdc", views.clhrdc, name="clhrdc"),
    # KABUHAYAN
    path("exhibit/kabuhayan/cashew", views.cashew, name="cashew"),
    path("exhibit/kabuhayan/doublemulching", views.double, name="double"),
    path("exhibit/kabuhayan/hydroponics", views.hydro, name="hydro"),
    path("exhibit/kabuhayan/zambelena", views.zambelena, name="zambelena"),
    path("exhibit/kabuhayan/empoweringwomen", views.women, name="women"),
    path("exhibit/kabuhayan/carrageenan", views.carra, name="carra"),
    path("exhibit/kabuhayan/solarpump", views.pump, name="pump"),
    path("exhibit/kabuhayan/starbooks", views.books, name="books"),
    path("exhibit/kabuhayan/mushroomforimprovement", views.mushroom, name="mushroom"),
    path("exhibit/kabuhayan/transplanting", views.transplant, name="transplant"),
    path("exhibit/kabuhayan/ecest", views.ecest, name="ecest"),
    path("exhibit/kabuhayan/floridablanca", views.florida, name="floridablanca"),
    path("exhibit/kabuhayan/snt", views.snt, name="snt"),
    path("exhibit/kabuhayan/sewing", views.sewing, name="sewing"),
    path("exhibit/kabuhayan/article1", views.article1, name="article1"),
    path("exhibit/kabuhayan/article2", views.article2, name="article2"),
    path("exhibit/kabuhayan/article3", views.article3, name="article3"),
    path("exhibit/kabuhayan/article4", views.article4, name="article4"),
    path("exhibit/kabuhayan/article5", views.article5, name="article5"),
    path("exhibit/kabuhayan/article6", views.article6, name="article6"),
    path("exhibit/kabuhayan/article7", views.article7, name="article7"),
    path("exhibit/kabuhayan/sntservices", views.sntservice, name="sntservice"),
    path("exhibit/kabuhayan/setup2.0", views.setup, name="setup"),
    path("exhibit/kabuhayan/successstories", views.stories, name="stories"),
    path("exhibit/kabuhayan/products", views.products, name="products"),
    path("exhibit/kabuhayan/story", views.story, name="story"),
    path("exhibit/kabuhayan/smarthybrid", views.smart, name="smart"),
    path("exhibit/kabuhayan/livelihood", views.live, name="live"),
    path("exhibit/kabuhayan/technologies", views.tech, name="tech"),
    # ADMIN PANEL
    path("dostr3adminpanel/", views.admin, name="dostr3adminpanellogin"),
    path("logout/", views.logoutAdmin, name="logout"),
    path("dostr3adminpanel/dashboard/", views.panel, name="dostr3admindahsboard"),
    path("dostr3adminpanel/visitors/", views.visitorTable, name="visitortable"),
    path("dostr3adminpanel/surveys/", views.surveyTable, name="surveytable"),
]

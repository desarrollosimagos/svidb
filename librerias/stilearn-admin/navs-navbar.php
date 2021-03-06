<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Stilearn Admin Bootstrap</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="stilearning">

        <meta http-equiv="x-pjax-version" content="v173">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
        <!-- fav and touch icons -->
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/favico-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/favico-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/favico-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="ico/favico-57-precomposed.png">
        <link rel="shortcut icon" href="ico/favico.png">
        <link rel="shortcut icon" href="http://wrapui.com/items/preview/stilearn-admin/ico/favico.ico">

        <link rel="stylesheet" href="styles/9281c719.vendor.css"/>        
        <link rel="stylesheet" href="styles/3fc417cd.main.css"/>
        
        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
          <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.min.js"></script>
        <![endif]-->
    </head>

    <body class="animated fadeIn">
        <!-- section header -->
        <header class="header">
            <!-- header brand -->
            <div class="header-brand">
                <!-- <h2><a data-pjax=".content-body" href="index.php"><span class="text-primary">Sti</span>learn</a></h2> -->
                <a data-pjax=".content-body" href="index.php">
                    <img class="brand-logo" src="images/dummy/8986f28e.stilearn-logo.png" alt="Stilearn Admin Sample Logo">
                </a>
            </div><!-- header brand -->
            
            <!-- header-profile -->
            <div class="header-profile">
                <div class="profile-nav">
                    <span class="profile-username">Bent</span>
                    <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="navs-navbar.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="navs-navbar.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="navs-navbar.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="navs-navbar.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
                    </ul>
                </div>
                <div class="profile-picture">
                    <img alt="me" src="images/dummy/0c31c9dc.profile.jpg">
                </div>
            </div><!-- header-profile -->

            <form role="form" class="form-inline">
                <button type="button" class="btn btn-default btn-expand-search"><i class="fa fa-search"></i></button>
                <div class="toggle-search">
                    <input type="text" class="form-control" placeholder="Search something">    
                    <button type="button" class="btn btn-default btn-collapse-search"><i class="fa fa-times"></i></button>
                </div>
            </form><!--/form-search-->

            <!-- header menu -->
            <ul class="hidden-xs header-menu pull-right">
                <li>
                    <a href="navs-navbar.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="navs-navbar.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="navs-navbar.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="navs-navbar.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="navs-navbar.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="navs-navbar.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="navs-navbar.php#">
                                <div class="notif-text pull-right">12%</div>
                                <div class="notif-text">Error</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="12" aria-valuemin="0" aria-valuemax="100" style="width: 12%">
                                        <span class="sr-only">12% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="navs-navbar.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all Tasks
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
            </ul><!--/header-menu pull-right-->
        </header><!--/header-->

        
        <!-- content section -->
        <section class="section">
            <!-- DONT FORGET REPLACE IT FOR PRODUCTION! -->
            <aside class="side-left">
                <ul class="sidebar">
                    <li>
                        <a href="index.php" data-pjax=".content-body">
                            <i class="sidebar-icon fa fa-home"></i>
                            <span class="sidebar-text">Dashboard</span>
                        </a>
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#">
                            <i class="sidebar-icon fa fa-magnet"></i>
                            <span class="sidebar-text">Interface</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="grid-system.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Grid System</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="typography.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Typography</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="buttons.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Buttons</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="icons.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Icons</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="modals.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Modals</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="tooltips-popovers.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Tooltips & Popovers</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="alerts-callouts.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Alerts & Callouts</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="progress-bars.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Progress Bars</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="labels-badge.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Labels & Badge</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="navs-navbar.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Navs & Navbar</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="animated.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Animated</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="loaders.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Loaders</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="helper-classes.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Helper</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#">
                            <div class="badge badge-primary animated animated-repeat wobble">3</div>
                            <i class="sidebar-icon fa fa-edit"></i>
                            <span class="sidebar-text">Form</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="form-basic.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Basic Form</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="form-elements.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Form Elements</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="form-validator.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Validator</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="form-wizard.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Wizard</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="form-uploader.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Uploader</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="form-editors.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Editor</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#">
                            <i class="sidebar-icon fa fa-bars"></i>
                            <span class="sidebar-text">Widgets</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="widget-panel.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Panels</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="widget-tabs.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Tabs</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="widget-collapse.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Collapse</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#">
                            <i class="sidebar-icon fa fa-files-o"></i>
                            <span class="sidebar-text">Pages</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="page-blank.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Blank Page</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="page-signin.php">
                                    <span class="sidebar-text">Signin</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="page-404.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Error 404</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="page-500.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Error 500</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="page-landing.php">
                                    <span class="sidebar-text">Landing Page</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="page-gallery.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Gallery</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="page-pricing.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Pricing</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="page-invoice.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Invoice</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#" data-pjax=".content-body">
                            <i class="sidebar-icon fa fa-bar-chart-o"></i>
                            <span class="sidebar-text">Charts</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="chart-flot.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Flot Charts</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="chart-morris.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Morris Charts</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="chart-inline.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Inline Charts</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#" data-pjax=".content-body">
                            <i class="sidebar-icon fa fa-table"></i>
                            <span class="sidebar-text">Tables</span>
                        </a>
                        <ul class="sidebar-child animated flipInY">
                            <li>
                                <a href="table-basic.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Basic Table</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="table-datatables.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Datatables</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="table-sorter.php" data-pjax=".content-body">
                                    <span class="sidebar-text">Table Sorter</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                    <li>
                        <a href="navs-navbar.php#">
                            <div class="badge badge-primary animated animated-repeat wobble">5</div>
                            <i class="sidebar-icon fa fa-th-large"></i>
                            <span class="sidebar-text">More</span>
                        </a>
                        <ul class="sidebar-child-inline animated flipInX">
                            <li>
                                <a href="calendar.php" data-pjax=".content-body">
                                    <i class="sidebar-icon fa fa-calendar-o"></i>
                                    <span class="sidebar-text">Calendar</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="maps.php" data-pjax=".content-body">
                                    <i class="sidebar-icon fa fa-map-marker"></i>
                                    <span class="sidebar-text">Maps</span>
                                </a>
                            </li><!--/child-item-->
                            <li>
                                <a href="masonry.php" data-pjax=".content-body">
                                    <i class="sidebar-icon fa fa-magic"></i>
                                    <span class="sidebar-text">Masonry</span>
                                </a>
                            </li><!--/child-item-->
                            <li class="divider"></li>
                            <li>
                                <a href="pjax.php" data-pjax=".content-body">
                                    <i class="sidebar-icon fa fa-play"></i>
                                    <span class="sidebar-text">PJAX</span>
                                </a>
                            </li><!--/child-item-->
                        </ul><!--/sidebar-child-->
                    </li><!--/sidebar-item-->
                </ul><!--/sidebar-->
            </aside><!--/side-left-->

            <div class="content">
                <div class="content-header">
                    <div class="content-header-extra">
                        <a class="item-ch-extra" href="navs-navbar.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="navs-navbar.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="navs-navbar.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#49AFCD" data-value="0,6,5,9,7,3,5,2,5,3,9"></span>
                            <div class="data-text text-info">
                                4367 <p class="text-muted">Orders</p>
                            </div>
                        </a><!--/item-ch-extra-->
                    </div><!--/content-header-extra -->

                    <h2 class="content-title"><i class="fa fa-home"></i> Welcome to Stilearn 2.0</h2>
                </div><!--/content-header -->
                
                <!-- content-control -->
                <div class="content-control">
                    <!--control-nav-->
                    <ul class="control-nav pull-right">
                        <li class="divider"></li>
                        <li>
                            <a href="navs-navbar.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="navs-navbar.php#">Some Action</a></li>
                                <li><a href="navs-navbar.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="navs-navbar.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="navs-navbar.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="navs-navbar.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- NAV & NAVBAR
                    ================================================== -->
                    <!-- NAVBAR -->
                    <div id="panel-navbar" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-navbar" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-navbar" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-navbar" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Navbar</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p class="text-muted"><strong>Navbar Default</strong></p>
                            <p>Navbars are responsive meta components that serve as navigation headers for your application or site. They begin collapsed (and are toggleable) in mobile views and become horizontal as the available viewport width increases. More detail about the <a rel="tooltip" title="Bootstrap navbar" target="_blank" href="http://getbootstrap.com/components/#navbar">Navbar</a>.</p>
                            <br>
                            <nav class="navbar navbar-default" role="navigation">
                                <!-- Brand and toggle get grouped for better mobile display -->
                                <div class="navbar-header">
                                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-1">
                                        <span class="sr-only">Toggle navigation</span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                    </button>
                                    <a class="navbar-brand" href="navs-navbar.php#">Stilearn</a>
                                </div><!--/navbar-header-->

                                <!-- Collect the nav links, forms, and other content for toggling -->
                                <div class="collapse navbar-collapse" id="navbar-collapse-1">
                                    <ul class="nav navbar-nav">
                                        <li class="active"><a href="navs-navbar.php#">Link</a></li>
                                        <li class="dropdown">
                                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                            <ul class="dropdown-menu animated fadeInDown" role="menu">
                                                <li><a href="navs-navbar.php#">Action</a></li>
                                                <li><a href="navs-navbar.php#">Another action</a></li>
                                                <li><a href="navs-navbar.php#">Something else here</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">Separated link</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">One more separated link</a></li>
                                            </ul>
                                        </li>
                                    </ul><!--/navbar-nav-->

                                    <form class="navbar-form navbar-left" role="search">
                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="Search">
                                        </div>
                                        <button type="submit" class="btn btn-primary">Submit</button>
                                    </form><!--/navbar-form-->

                                    <ul class="nav navbar-nav navbar-right">
                                        <li class="dropdown">
                                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                            <ul class="dropdown-menu animated fadeInDown" role="menu">
                                                <li><a href="navs-navbar.php#">Action</a></li>
                                                <li><a href="navs-navbar.php#">Another action</a></li>
                                                <li><a href="navs-navbar.php#">Something else here</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">Separated link</a></li>
                                            </ul>
                                        </li>
                                    </ul><!--/navbar-nav right-->
                                </div><!-- /.navbar-collapse -->
                            </nav><!--/navbar-->
                            <br>


                            <p class="text-muted"><strong>Navbar inverse</strong></p>
                            <p>Modify the look of the navbar by adding <code>.navbar-inverse</code></p>
                            <br>
                            <nav class="navbar navbar-inverse" role="navigation">
                                <!-- Brand and toggle get grouped for better mobile display -->
                                <div class="navbar-header">
                                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-2">
                                        <span class="sr-only">Toggle navigation</span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                    </button>
                                    <a class="navbar-brand" href="navs-navbar.php#">Stilearn</a>
                                </div><!--/navbar-header-->

                                <!-- Collect the nav links, forms, and other content for toggling -->
                                <div class="collapse navbar-collapse" id="navbar-collapse-2">
                                    <ul class="nav navbar-nav">
                                        <li class="active"><a href="navs-navbar.php#">Link</a></li>
                                        <li class="dropdown">
                                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                            <ul class="dropdown-menu animated fadeInDown" role="menu">
                                                <li><a href="navs-navbar.php#">Action</a></li>
                                                <li><a href="navs-navbar.php#">Another action</a></li>
                                                <li><a href="navs-navbar.php#">Something else here</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">Separated link</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">One more separated link</a></li>
                                            </ul>
                                        </li>
                                    </ul><!--/navbar-nav-->

                                    <form class="navbar-form navbar-left" role="search">
                                        <div class="form-group">
                                            <input type="text" class="form-control" placeholder="Search">
                                        </div>
                                        <button type="submit" class="btn btn-danger">Submit</button>
                                    </form><!--/navbar-form-->

                                    <ul class="nav navbar-nav navbar-right">
                                        <li class="dropdown">
                                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                                            <ul class="dropdown-menu animated fadeInDown" role="menu">
                                                <li><a href="navs-navbar.php#">Action</a></li>
                                                <li><a href="navs-navbar.php#">Another action</a></li>
                                                <li><a href="navs-navbar.php#">Something else here</a></li>
                                                <li class="divider"></li>
                                                <li><a href="navs-navbar.php#">Separated link</a></li>
                                            </ul>
                                        </li>
                                    </ul><!--/navbar-nav right-->
                                </div><!-- /.navbar-collapse -->
                            </nav><!--/navbar-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-navbar -->




                    <!-- NAV -->
                    <div id="panel-navs" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-navs" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-navs" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-navs" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Navs</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Starting with the base <code>.nav</code> class, as well as shared states. Swap modifier classes to switch between each style.</p>

                            <h4>Tabs</h4>
                            <p>Note the <code>.nav-tabs</code> class requires the <code>.nav</code> base class.</p><br>
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="navs-navbar.php#">Home</a></li>
                                <li><a href="navs-navbar.php#">Profile</a></li>
                                <li class="dropdown">
                                    <a class="dropdown-toggle" data-toggle="dropdown" href="navs-navbar.php#">
                                        Dropdown <i class="fa fa-angle-down"></i>
                                    </a>
                                    <ul class="dropdown-menu animated flipInX" role="menu">
                                        <li><a href="navs-navbar.php#">Action</a></li>
                                        <li><a href="navs-navbar.php#">Another action</a></li>
                                        <li><a href="navs-navbar.php#">Something else here</a></li>
                                        <li class="divider"></li>
                                        <li><a href="navs-navbar.php#">Separated link</a></li>
                                    </ul>
                                </li>
                            </ul>
                            <br>
                            <pre class="prettyprint no-padding">&lt;ul class=&quot;nav nav-tabs&quot;&gt;
    &lt;li class=&quot;active&quot;&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Profile&lt;/a&gt;&lt;/li&gt;
    &lt;li class=&quot;dropdown&quot;&gt;
        &lt;a class=&quot;dropdown-toggle&quot; data-toggle=&quot;dropdown&quot; href=&quot;#&quot;&gt;
            Dropdown &lt;span class=&quot;caret&quot;&gt;&lt;/span&gt;
        &lt;/a&gt;
        &lt;ul class=&quot;dropdown-menu&quot;&gt;
            ...
        &lt;/ul&gt;
    &lt;/li&gt;
&lt;/ul&gt;</pre><br>

                        
                            <h4>Pills</h4>
                            <p>Take that same HTML, but use <code>.nav-pills</code> instead:</p><br>
                            <ul class="nav nav-pills">
                                <li class="active"><a href="navs-navbar.php#">Home</a></li>
                                <li><a href="navs-navbar.php#">Profile</a></li>
                                <li class="dropdown">
                                    <a class="dropdown-toggle" data-toggle="dropdown" href="navs-navbar.php#">
                                        Dropdown <i class="fa fa-angle-down"></i>
                                    </a>
                                    <ul class="dropdown-menu animated flipInX" role="menu">
                                        <li><a href="navs-navbar.php#">Action</a></li>
                                        <li><a href="navs-navbar.php#">Another action</a></li>
                                        <li><a href="navs-navbar.php#">Something else here</a></li>
                                        <li class="divider"></li>
                                        <li><a href="navs-navbar.php#">Separated link</a></li>
                                    </ul>
                                </li>
                            </ul>
                            <br>
                            <pre class="prettyprint no-padding">&lt;ul class=&quot;nav nav-pills&quot;&gt;
    &lt;li class=&quot;active&quot;&gt;&lt;a href=&quot;#&quot;&gt;Home&lt;/a&gt;&lt;/li&gt;
    &lt;li&gt;&lt;a href=&quot;#&quot;&gt;Profile&lt;/a&gt;&lt;/li&gt;
    &lt;li class=&quot;dropdown&quot;&gt;
        &lt;a class=&quot;dropdown-toggle&quot; data-toggle=&quot;dropdown&quot; href=&quot;#&quot;&gt;
            Dropdown &lt;span class=&quot;caret&quot;&gt;&lt;/span&gt;
        &lt;/a&gt;
        &lt;ul class=&quot;dropdown-menu&quot;&gt;
            ...
        &lt;/ul&gt;
    &lt;/li&gt;
&lt;/ul&gt;</pre><br>
                            <p>Pills are also vertically stackable. Just add <code>.nav-stacked</code>.</p>
                            <ul class="nav nav-pills nav-stacked" style="max-width: 300px">
                                <li class="active"><a href="navs-navbar.php#">Home</a></li>
                                <li><a href="navs-navbar.php#">Profile</a></li>
                                <li><a href="navs-navbar.php#">Messages</a></li>
                            </ul>
                            <br>
                            <pre class="prettyprint no-padding">&lt;ul class=&quot;nav nav-pills nav-stacked&quot;&gt;
    ...
&lt;/ul&gt;</pre><br>
                        
                            <h4>Justified</h4>
                            <p>Easily make tabs or pills equal widths of their parent at screens wider than 768px with <code>.nav-justified</code>. On smaller screens, the nav links are stacked.</p>
                            <div class="callout callout-warning">
                                <h4>Safari and responsive justified navs</h4>
                                <p>Safari exhibits a bug in which resizing your browser horizontally causes rendering errors in the justified nav that are cleared upon refreshing. This bug is also shown in the <a rel="tooltip" title="Refer to BS example" target="_blank" href="http://getbootstrap.com/examples/justified-nav/">justified nav example</a>.</p>
                            </div>
                            <br>
                            <ul class="nav nav-tabs nav-justified">
                                <li class="active"><a href="navs-navbar.php#">Home</a></li>
                                <li><a href="navs-navbar.php#">Profile</a></li>
                                <li><a href="navs-navbar.php#">Messages</a></li>
                            </ul>
                            <br>
                            <ul class="nav nav-pills nav-justified">
                                <li class="active"><a href="navs-navbar.php#">Home</a></li>
                                <li><a href="navs-navbar.php#">Profile</a></li>
                                <li><a href="navs-navbar.php#">Messages</a></li>
                            </ul>
                        </div><!-- /panel-body -->
                    </div><!-- /panel-navs -->





                    <!-- LIST GROUP -->
                    <div id="panel-listgroup" class="panel panel-default">
                        <div class="panel-heading bg-white">
                            <div class="panel-actions">
                                <button data-refresh="#panel-listgroup" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-listgroup" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-listgroup" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">List Group</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p class="lead">List groups are a flexible and powerful component for displaying not only simple lists of elements, but complex ones with custom content.</p>
                            <p>The most basic list group is simply an unordered list with list items, and the proper classes. Build upon it with the options that follow, or your own CSS 
                            </p><p>Add the badges component to any list group item and it will automatically be positioned on the right.</p>
                            <ul class="list-group" data-toggle="sortable-list" style="max-width: 320px">
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge">14</span>Hover on Badge and drag it</li>
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge badge-primary">8</span>Dapibus ac facilisis in</li>
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge badge-success">32</span>Morbi leo risus</li>
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge badge-info">2</span>Porta ac consectetur ac</li>
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge badge-warning">9</span>Vestibulum at eros</li>
                                <li class="list-group-item sortable-list-item"><span class="sortable-list-handle badge badge-danger">11</span>Consectetur adipisicing</li>
                            </ul>
                            <p><strong>NOTE: </strong> Adding sortable support via attribute <code>data-toggle="sortable-list"</code>. Refer to the demo to see this in action.</p>
                            <pre class="prettyprint no-padding">&lt;ul class=&quot;list-group&quot;&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge&quot;&gt;14&lt;/span&gt;
        Cras justo odio
    &lt;/li&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-primary&quot;&gt;8&lt;/span&gt;
        Dapibus ac facilisis in
    &lt;/li&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-success&quot;&gt;32&lt;/span&gt;
        Morbi leo risus
    &lt;/li&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-info&quot;&gt;2&lt;/span&gt;
        Porta ac consectetur ac
    &lt;/li&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-warning&quot;&gt;9&lt;/span&gt;
        Vestibulum at eros
    &lt;/li&gt;
    &lt;li class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-danger&quot;&gt;11&lt;/span&gt;
        Consectetur adipisicing
    &lt;/li&gt;
&lt;/ul&gt;</pre><br>


                            <h4>Linked items</h4>
                            <p>Linkify list group items by using anchor tags instead of list items (that also means a parent <code>&lt;div&gt;</code> instead of an <code>&lt;ul&gt;</code>). No need for individual parents around each element.</p>
                            <div class="list-group" style="max-width: 320px">
                                <a href="navs-navbar.php#" class="list-group-item"><span class="badge">14</span>Cras justo odio</a>
                                <a href="navs-navbar.php#" class="list-group-item"><span class="badge badge-primary">8</span>Dapibus ac facilisis in</a>
                                <a href="navs-navbar.php#" class="list-group-item"><span class="badge badge-success">32</span>Morbi leo risus</a>
                                <a href="navs-navbar.php#" class="list-group-item active"><span class="badge badge-info">2</span>Porta ac consectetur ac</a>
                                <a href="navs-navbar.php#" class="list-group-item"><span class="badge badge-warning">9</span>Vestibulum at eros</a>
                                <a href="navs-navbar.php#" class="list-group-item"><span class="badge badge-danger">11</span>Consectetur adipisicing</a>
                            </div>
                            <pre class="prettyprint no-padding">&lt;div class=&quot;list-group&quot;&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge&quot;&gt;14&lt;/span&gt;
        Cras justo odio
    &lt;/a&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-primary&quot;&gt;8&lt;/span&gt;
        Dapibus ac facilisis in
    &lt;/a&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item active&quot;&gt;
        &lt;span class=&quot;badge badge-success&quot;&gt;32&lt;/span&gt;
        Morbi leo risus
    &lt;/a&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-info&quot;&gt;2&lt;/span&gt;
        Porta ac consectetur ac
    &lt;/a&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-warning&quot;&gt;9&lt;/span&gt;
        Vestibulum at eros
    &lt;/a&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item&quot;&gt;
        &lt;span class=&quot;badge badge-danger&quot;&gt;11&lt;/span&gt;
        Consectetur adipisicing
    &lt;/a&gt;
&lt;/div&gt;</pre><br>

                            
                            <h4>Simple custom content</h4>
                            <div class="list-group">
                                <a href="navs-navbar.php#" class="list-group-item active">
                                    <h4 class="list-group-item-heading">List group item heading</h4>
                                    <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                                </a>
                                <a href="navs-navbar.php#" class="list-group-item">
                                    <h4 class="list-group-item-heading">List group item heading</h4>
                                    <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                                </a>
                                <a href="navs-navbar.php#" class="list-group-item">
                                    <h4 class="list-group-item-heading">List group item heading</h4>
                                    <p class="list-group-item-text">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>
                                </a>
                            </div>
                            <pre class="prettyprint no-padding">&lt;div class=&quot;list-group&quot;&gt;
    &lt;a href=&quot;#&quot; class=&quot;list-group-item active&quot;&gt;
        &lt;h4 class=&quot;list-group-item-heading&quot;&gt;List group item heading&lt;/h4&gt;
        &lt;p class=&quot;list-group-item-text&quot;&gt;...&lt;/p&gt;
    &lt;/a&gt;
&lt;/div&gt;</pre>
                        </div><!-- /panel-body -->
                    </div><!-- /panel-listgroup -->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="navs-navbar.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="navs-navbar.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="navs-navbar.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="navs-navbar.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="navs-navbar.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="navs-navbar.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="navs-navbar.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="navs-navbar.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
                        <i class="fa fa-circle-o text-primary"></i> 
                        Phillip Morrison
                    </h3><!-- /chatbox-heading -->

                    <div class="chatbox-body" data-toggle="niceScroll">

                        <div class="chat-separate"><time class="chat-time" datetime="">Jan 9, 2014</time></div>

                        <div class="chat-in">
                            <div class="chat-user">Phillip Morrison</div>
                            <div class="chat-msg">
                                <p>Praesent cras quisque. Volutpat sit interdum. Magnis leo, duis faucibus eu, in rutrum nulla. Eget sed, dolor nibh. Vero mi habitant</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">01:14 PM</time>
                            </div>
                        </div><!-- /chat-in -->

                        <div class="chat-out">
                            <div class="chat-user">Me</div>
                            <div class="chat-msg">
                                <p>Dictum at aenean, faucibus euismod convallis. Ipsum nec, platea amet nulla.</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">01:16 PM</time>
                            </div>
                        </div><!-- /chat-out -->

                        <div class="chat-in">
                            <div class="chat-user">Phillip Morrison</div>
                            <div class="chat-msg">
                                <p>Eu augue, proin rutrum. Et vehicula, wisi fusce, ut ipsum</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">01:20 PM</time>
                            </div>
                        </div><!-- /chat-in -->

                        <div class="chat-separate"><time class="chat-time" datetime="">Jan 14, 2014</time></div>

                        <div class="chat-out">
                            <div class="chat-user">Me</div>
                            <div class="chat-msg">
                                <p>Est penatibus pellentesque, augue tincidunt, a suspendisse</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">09:36 AM</time>
                            </div>
                        </div><!-- /chat-out -->

                        <div class="chat-in">
                            <div class="chat-user">Phillip Morrison</div>
                            <div class="chat-msg">
                                <p>Nunc nulla. Donec laoreet non, lobortis praesent</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">09:40 AM</time>
                            </div>
                        </div><!-- /chat-in -->

                        <div class="chat-separate"><time class="chat-time" datetime="">Recent</time></div>

                        <div class="chat-in">
                            <div class="chat-user">Phillip Morrison</div>
                            <div class="chat-msg">
                                <p>Dui posuere. Reprehenderit felis libero, potenti vitae</p>
                                <time class="chat-time" datetime="2013-12-13T20:00">12 min</time>
                            </div>
                        </div><!-- /chat-out -->

                    </div><!-- /chatbox-body -->

                    <div class="chatbox-footer">
                        <form class="chat-form">
                            <p class="chat-status"><i class="fa fa-spinner fa-spin"></i> Phillip Morrison is type...</p>
                            <div class="form-group">
                                <button type="submit" class="btn" title="Send"><i class="fa fa-share"></i></button>
                                <input type="text" class="chat-input" name="send_chat" placeholder="Type a message">
                            </div>
                        </form>
                    </div><!-- /chatbox -->
                </div><!-- /chatbox -->
            </div><!-- /module -->
        </aside><!--/side-right -->


        <!-- section footer -->
        <a rel="to-top" href="navs-navbar.php#top"><i class="fa fa-arrow-up"></i></a>
        <footer>
            <p>&copy; 2014 Stilearning. <small><a target="_blank" href="https://wrapbootstrap.com/theme/stilearn-admin-template-WB0TFD2S0">Purchase</a> this template only <strong>$18</strong></small></p>
        </footer>



        <!-- javascript
        ================================================== -->
        <script src="scripts/39914ff3.vendor-main.js"></script>        
        <script src="scripts/756399db.vendor-usefull.js"></script>
        <script src="scripts/e7058f60.vendor-form.js"></script>        
        <script src="scripts/fc9d433c.vendor-editor.js"></script>        
        <!--[if lte IE 8]>
        <script src="scripts/eae815b5.excanvas.js"></script>
        <![endif]-->
        <script src="scripts/2ce1156c.vendor-graph.js"></script>    
        <script src="scripts/37a77790.vendor-table.js"></script>
        <script src="scripts/1581b2aa.vendor-maps.js"></script>        
        <script src="scripts/5f4fd25b.vendor-util.js"></script>


        <!-- required stilearn template js -->
        <script src="scripts/5917523f.main.js"></script>
        <!-- This scripts will be reload after pjax or if popstate event is active (use with class .re-execute) -->
        <script src="scripts/89c3d6c9.initializer.js"></script>
        
        <script>
          (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
          function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
          e=o.createElement(i);r=o.getElementsByTagName(i)[0];
          e.src='//www.google-analytics.com/analytics.js';
          r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
          ga('create','UA-48454066-1');ga('send','pageview');
        </script>

    </body>
</html>
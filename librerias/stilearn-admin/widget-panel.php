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
                    <a href="widget-panel.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="widget-panel.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="widget-panel.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="widget-panel.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="widget-panel.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="widget-panel.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="widget-panel.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="widget-panel.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="widget-panel.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="widget-panel.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="widget-panel.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="widget-panel.php#">
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
                            <a class="view-all" tabindex="-1" href="widget-panel.php#">
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
                        <a href="widget-panel.php#">
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
                        <a href="widget-panel.php#">
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
                        <a href="widget-panel.php#">
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
                        <a href="widget-panel.php#">
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
                        <a href="widget-panel.php#" data-pjax=".content-body">
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
                        <a href="widget-panel.php#" data-pjax=".content-body">
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
                        <a href="widget-panel.php#">
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
                        <a class="item-ch-extra" href="widget-panel.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="widget-panel.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="widget-panel.php#">
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
                            <a href="widget-panel.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="widget-panel.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="widget-panel.php#">Some Action</a></li>
                                <li><a href="widget-panel.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="widget-panel.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="widget-panel.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="widget-panel.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- Widget Panel
                    ================================================== -->
                    <div class="row">
                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div id="panel-default" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-default" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-default" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-default" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-default" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Default panel</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Widget Panel comes with four basic functions (close, collapse, expand, refresh). Panel allows you to enable support for <a rel="tooltip" title="View jquery-ui sortable doc" target="_blank" href="http://jqueryui.com/sortable/">jquery-ui sortable</a> by adding a class <code>.sortable-item</code> to Panel <i>(assuming you have added an attribute <code>data-toggle="sortable"</code> to the Panel parent)</i>. Click and drag Panel Icon to se how it work!
                                    </p>
                                    <p>How to make a basic Panel? Please see <a rel="tooltip" title="Bootstrap panel" target="_blank" href="http://getbootstrap.com/components/#panels">Bootstrap docs</a> about Panel.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Widget Panel <i>footer</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-default -->


                            <div id="panel-close" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-close="#panel-close" data-animate="hinge" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Panel close <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Panel actions close support with animate.css (only exits animation) by <strong>Dan Eden</strong>. Add attribute <code>data-animate="animateOutName"</code> to the action close button to activate custom animate close Panel.
                                    </p>
                                    <p>If you close the Panel it same you adding class <code>.hide</code> to Panel. Just remove class <code>.hide</code> to show it again.</p>
                                    <p>Support all of <a rel="tooltip" title="Animate.css" target="_blank" href="https://daneden.me/animate/">Animate.css</a></p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-close -->


                            <div id="panel-expand" class="panel panel-default">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group">
                                            <button title="expand" class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-expand"></i>
                                            </button>
                                            <ul class="dropdown-menu pull-right">
                                                <li><a href="widget-panel.php#" data-expand="#panel-expand">Expand</a></li>
                                                <li><a href="widget-panel.php#" data-expand="#panel-expand" data-expand-mode="fullscreen">Expand to fullscreen</a></li>
                                            </ul>
                                        </div>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars"></i> Expand <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Expand make a widget to toggle full window or fullscreen. Add attribute <code>data-expand="#panel-id"</code> to activate it, adding attribute <code>data-expand-mode="fullscreen"</code> to fullscreen mode. Expand feature also allow you to hide/show a element on screen toggle by adding class <code>.hide-on-expand</code> or <code>.show-on-expand</code></p>
                                    
                                    <div class="alert alert-success show-on-expand">
                                        <h4>This block show on expand</h4>
                                        <p>Commodo lobortis. Nascetur sed, fringilla dolor, etiam feugiat massa. Mauris tortor suspendisse, mauris etiam vitae. Quam in sunt. Tempor ultrices lacinia. Velit dis.</p>
                                    </div>
                                    <div class="alert alert-info hide-on-expand">
                                        <h4>This block hide on expand</h4>
                                        <p>Ridiculus tristique sed, feugiat tortor commodo. Mollis urna, ac hendrerit egestas, et adipiscing. Phasellus id pharetra. At dui, eget convallis, accumsan elementum. Adipiscing pellentesque. Purus vestibulum urna.</p>
                                    </div>
                                    <p>Fullscreen <a rel="tooltip" title="caniuse" href="http://caniuse.com/fullscreen" target="_parent">Support browsers</a>. <br><i>Safari 5.1 doesn't support use of the keyboard in fullscreen</i>.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Not allow <i>Sortable</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-expand -->


                            <div id="panel-table" class="panel panel-default">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-table" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-table" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-table" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-table" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars"></i> With table <small>no-sortable</small></h3>
                                </div><!-- /panel-heading -->

                                <!-- Table -->
                                <table class="tablesorter table">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>First Name</th>
                                            <th>Last Name</th>
                                            <th>Username</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Mark</td>
                                            <td>Otto</td>
                                            <td>@mdo</td>
                                        </tr>
                                        <tr>
                                            <td>2</td>
                                            <td>Jacob</td>
                                            <td>Thornton</td>
                                            <td>@fat</td>
                                        </tr>
                                        <tr>
                                            <td>3</td>
                                            <td>Larry</td>
                                            <td>the Bird</td>
                                            <td>@twitter</td>
                                        </tr>
                                    </tbody>
                                    <tfoot>
                                        <tr>
                                            <th colspan="4" class="ts-pager form-horizontal">
                                                <button type="button" class="btn btn-default btn-sm first"><i class="icon-step-backward fa fa-angle-double-left"></i></button>
                                                <button type="button" class="btn btn-default btn-sm prev"><i class="icon-arrow-left fa fa-angle-left"></i></button>
                                                <span class="pagedisplay"></span> <!-- this can be any element, including an input -->
                                                <button type="button" class="btn btn-default btn-sm next"><i class="icon-arrow-right fa fa-angle-right"></i></button>
                                                <button type="button" class="btn btn-default btn-sm last"><i class="icon-step-forward fa fa-angle-double-right"></i></button>
                                                <select class="pagesize input-sm" title="Select page size">
                                                    <option value="5" selected="selected">5</option>
                                                    <option value="10">10</option>
                                                    <option value="25">25</option>
                                                    <option value="50">50</option>
                                                </select>
                                                <select class="pagenum input-sm" title="Select page number"></select>
                                            </th>
                                        </tr>
                                    </tfoot>
                                </table><!-- /table -->

                                <div class="panel-footer hide-on-expand">Easily include <a rel="tooltip" title="Basic Table" data-pjax=".content-body" data-animatedpjax="fadeInUp" href="table-basic.php">table</a> within any Panel.</div>
                            </div><!-- /panel-table -->


                            <div id="panel-sortable" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-sortable" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-sortable" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-sortable" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-sortable" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Sortable handler</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magni, at, deserunt, eveniet, iure aperiam tempore facilis quam ut beatae dolores voluptate error voluptatibus quis minus repellendus qui commodi sint! Inventore.</p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-sortable -->


                            <div id="panel-withbtn" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="copy" class="btn btn-default btn-sm"><i class="fa fa-copy"></i></button>
                                        <button rel="tooltip-bottom" title="cut" class="btn btn-default btn-sm"><i class="fa fa-cut"></i></button>
                                        <button rel="tooltip-bottom" title="paste" class="btn btn-default btn-sm"><i class="fa fa-paste"></i></button>
                                    </div><!-- /btn-group -->
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="create new file" class="btn btn-default btn-sm"><i class="fa fa-file"></i></button>
                                        <button rel="tooltip-bottom" title="open from folder" class="btn btn-default btn-sm"><i class="fa fa-folder-open-o"></i></button>
                                        <button rel="tooltip-bottom" title="save" class="btn btn-default btn-sm"><i class="fa fa-save"></i></button>
                                    </div><!-- /btn-group -->
                                    <h3 class="panel-title sortable-widget-handle">Play with button</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-helper-block">
                                    <button data-refresh="#panel-withbtn" rel="tooltip-bottom" title="refresh" class="btn btn-default btn-sm pull-right"><i class="fa fa-refresh"></i></button>
                                    <div class="btn-group" data-toggle="buttons">
                                        <button rel="tooltip-bottom" title="bold" class="btn btn-default btn-sm"><i class="fa fa-bold"></i></button>
                                        <button rel="tooltip-bottom" title="italic" class="btn btn-default btn-sm"><i class="fa fa-italic"></i></button>
                                        <button rel="tooltip-bottom" title="underline" class="btn btn-default btn-sm"><i class="fa fa-underline"></i></button>
                                        <button rel="tooltip-bottom" title="strikethrough" class="btn btn-default btn-sm"><i class="fa fa-strikethrough"></i></button>
                                    </div>
                                    <div class="btn-group">
                                        <button rel="tooltip-bottom" title="list-ol" class="btn btn-default btn-sm"><i class="fa fa-list-ol"></i></button>
                                        <button rel="tooltip-bottom" title="list-ul" class="btn btn-default btn-sm"><i class="fa fa-list-ul"></i></button>
                                        <button rel="tooltip-bottom" title="table" class="btn btn-default btn-sm"><i class="fa fa-table"></i></button>
                                    </div>
                                    <div class="btn-group" data-toggle="buttons">
                                        <button rel="tooltip-bottom" title="align-center" class="btn btn-default btn-sm"><i class="fa fa-align-center"></i></button>
                                        <button rel="tooltip-bottom" title="align-justify" class="btn btn-default btn-sm"><i class="fa fa-align-justify"></i></button>
                                        <button rel="tooltip-bottom" title="align-left" class="btn btn-default btn-sm"><i class="fa fa-align-left"></i></button>
                                        <button rel="tooltip-bottom" title="align-right" class="btn btn-default btn-sm"><i class="fa fa-align-right"></i></button>
                                    </div>
                                </div>
                                
                                <form class="single-editor" role="form">
                                    <textarea class="form-control single-editor" placeholder="Type something.."></textarea>
                                </form>
                                <div class="panel-body">
                                    <p>Easily Use button like a toolbar, best support with <code>.btn-sm</code> and <code>.btn-xs</code></p>
                                    <p>Please click on <strong>update</strong> button below!</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer clearfix">
                                    <div class="pull-right">
                                        <button class="btn btn-warning btn-sm">Cancel</button>
                                        <button data-refresh="#panel-withbtn" class="btn btn-primary btn-sm">Update</button>
                                    </div>
                                </div>
                            </div><!-- /panel-withbtn -->
                        </div><!-- /cols -->



                        <div class="col-md-6" data-toggle="sortable-widget">
                            <div id="panel-context" class="panel panel-primary sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group open">
                                            <button title="Chose a color" class="btn-panel disable-tooltip dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-tint"></i>
                                            </button>
                                            <ul class="dropdown-menu dropdown-inline bg-midnight pull-right" role="menu">
                                                <li>
                                                    <a rel="tooltip" title="Default" data-context="panel-default" data-target="#panel-context" class="color-pick bg-cloud"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Primary" data-context="panel-primary" data-target="#panel-context" class="color-pick bg-primary"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Success" data-context="panel-success" data-target="#panel-context" class="color-pick bg-success"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Info" data-context="panel-info" data-target="#panel-context" class="color-pick bg-info"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Warning" data-context="panel-warning" data-target="#panel-context" class="color-pick bg-warning"></a>
                                                </li>
                                                <li>
                                                    <a rel="tooltip" title="Danger" data-context="panel-danger" data-target="#panel-context" class="color-pick bg-danger"></a>
                                                </li>
                                            </ul>
                                        </div>
                                        <button data-refresh="#panel-context" data-loader="loader-cloud" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-context" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-context" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-context" title="close" data-animate="flipOutX" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Contextual alternatives</h3>
                                </div><!-- /panel-heading -->
                                <div class="panel-body">
                                    <p>Easily make a panel more meaningful to a particular context by adding any of the contextual state classes (panel-primary, panel-success, panel-info, panel-warning, panel-danger). Please select a color to see contextual demo <i>(click on color chooser actions <span class="fa fa-tint"></span>)</i>.</p>
                                    <p>You can activate toggle contextual Panel by adding attributes <code>data-context="panel-context-class" data-target="#panel-id"</code> on your custom action.</p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer">
                                    Widget Panel <i>footer</i>
                                </div><!-- /panel-footer -->
                            </div><!-- /panel-context -->


                            <div id="panel-refresh" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <div class="btn-group">
                                            <button class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                                <i class="fa fa-refresh"></i>
                                            </button>
                                            <ul class="dropdown-menu pull-right">
                                                <li>
                                                    <a href="widget-panel.php#" data-refresh="#panel-refresh" data-url="data-sample/sample-plain-data.txt" data-target-place="#demo-target-refresh1">Basic Refresh</a>
                                                </li>
                                                <li>
                                                    <a href="widget-panel.php#" data-refresh="#panel-refresh" data-url="data-sample/sample-data.json" data-loader="loader-cloud" data-target-place="#demo-target-refresh2">Advance Refresh</a>
                                                </li>
                                                <li class="divider"></li>
                                                <li>
                                                    <a href="widget-panel.php#" data-refresh="#panel-refresh" data-url="data-sample/sample-datas.txt">Error case</a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Panel refresh <small>actions</small></h3>
                                </div><!-- /panel-heading -->
                                <div class="panel-body">
                                    <div id="demo-target-refresh1"></div>
                                    <p>
                                        Panel actions refresh allow you to update data inside Panel via ajax. Just add <code>data-refresh="#panel-id"</code> and see how it work. Targeting action url via attribute <code>data-url="path/target/file"</code> and custom loader type with attribute <code>data-loader="loader-name"</code> (See avilable <a data-pjax=".content-body" href="loaders.php">Loaders</a>).
                                    </p>
                                    <p>By default data will replace on Panel Body <code>.panel-body</code>, But you can customize it with attribute <code>data-target-place="#target-place"</code></p>
                                    <p><strong>NOTE: </strong><i>Sometime, you may get an error message when refreshing a Panel. If your Panel have Panel body, error message will placed on there. But if you not have Panel Body on your Panel, error will placed after Panel Heading</i>.</p>
                                </div><!-- /panel-body -->
                                <table class="table table-hover" id="demo-target-refresh2"></table>
                            </div><!-- /panel-refresh -->


                            <div id="panel-collapse" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-collapse" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Collapse <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Collapse just hide the Panel Body, Table and List Group inside Panel. If your panel have a footer, its not include on hide elements. When you want make it or other elements include to collapse, just add class <code>.panel-collapse-element</code>. Add attribute <code>data-collapse="#panel-id"</code> to actions button.
                                    </p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-collapse -->


                            <div id="panel-collapse2" class="panel panel-default panel-collapsed sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-collapse="#panel-collapse2" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Default Collapse <small>actions</small></h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body">
                                    <p>
                                        Add class <code>.panel-collapsed</code> to Panel when you want to collapse it by default.
                                    </p>
                                </div><!-- /panel-body -->

                                <div class="panel-footer panel-collapse-element">Include to collapse element</div>
                            </div><!-- /panel-collapse2 -->


                            <div id="panel-scrollnice" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-scrollnice" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-scrollnice" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-scrollnice" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-scrollnice" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Scroll nice</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body" style="height:200px" data-toggle="niceScroll" data-scroll-wrapper=".wrapper-scroll" data-scroll-cursorcolor="#ecf0f1">
                                    <div class="wrapper-scroll">
                                        <p>
                                            Just add attribute <code>data-toggle="niceScroll"</code> on Panel Body or other elements you want to make a Nice Scroll and define the scroll wrapper target <small>(required)</small> <code>data-scroll-wrapper=".wrapper-scroll"</code> <i>(can use with attribute class or id)</i>.
                                        </p>
                                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Possimus, dicta, sed quod veniam inventore nesciunt doloremque accusamus modi quasi tempore ratione excepturi cupiditate fuga iusto molestiae officiis saepe aperiam fugit qui neque culpa dolore aspernatur nemo totam quas dolorum dolor molestias autem quae quisquam.</p>
                                        <p> Consequatur, qui distinctio aperiam itaque sapiente amet quaerat hic. Quia, veritatis, assumenda, iste dolor laboriosam tenetur vitae neque illum sapiente esse expedita ipsum dolore tempora fugiat obcaecati consectetur facilis commodi fuga eveniet voluptates reprehenderit a culpa libero optio asperiores ad enim accusantium. Suscipit, aspernatur, laborum, ad cumque quos omnis quisquam inventore repudiandae fugiat alias aut qui?</p>
                                        <p> Consequatur, qui distinctio aperiam itaque sapiente amet quaerat hic. Quia, veritatis, assumenda, iste dolor laboriosam tenetur vitae neque illum sapiente esse expedita ipsum dolore tempora fugiat obcaecati consectetur facilis commodi fuga eveniet voluptates reprehenderit a culpa libero optio asperiores ad enim accusantium. Suscipit, aspernatur, laborum, ad cumque quos omnis quisquam inventore repudiandae fugiat alias aut qui?</p>
                                    </div>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-scrollnice -->


                            <div id="panel-listgroup" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
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
                                        <button data-close="#panel-listgroup" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> List group & slippylist</h3>
                                </div><!-- /panel-heading -->

                                <!-- List group -->
                                <ul class="list-group" data-toggle="slippylist">
                                    <li class="list-group-item">hold &amp; reorder</li>
                                    <li class="list-group-item no-reorder"><div class="badge pull-right">5</div>Swipe,</li>
                                    <li class="list-group-item no-swipe"><span class="slippylist-handle pull-right">or instantly</span> hold &amp; reorder</li>
                                    <li class="list-group-item">or either</li>
                                    <li class="list-group-item no-swipe no-reorder">or none of them.</li>
                                    <li class="list-group-item">Can play nicely with:</li>
                                    <li class="list-group-item">interaction <input style="position:relative;top:8px;margin-left:15px" type="range"></li>
                                    <li class="list-group-item" style="transform: scaleX(0.97) skewX(-10deg); -webkit-transform: scaleX(0.97) skewX(-10deg)">CSS transforms</li>
                                    <li class="list-group-item allow-select"><span class="no-reorder">and selectable text, even though animating elements with selected text is a bit weird.</span></li>
                                    <li class="list-group-item">iOS Safari</li>
                                    <li class="list-group-item">Android Firefox</li>
                                    <li class="list-group-item">Mobile Chrome</li>
                                    <li class="list-group-item">Oprea Presto and Blink</li>
                                </ul><!-- /list-group -->

                                <div class="panel-footer">Easily include full-width <a rel="tooltip" title="List Group" data-pjax=".content-body" data-animatedpjax="fadeInUp" href="navs-navbar.php#panel-listgroup">list groups</a> within any Panel.</div>
                            </div><!-- /panel-listgroup -->
                        </div><!-- /cols -->
                    </div><!-- /row -->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="widget-panel.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="widget-panel.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="widget-panel.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="widget-panel.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="widget-panel.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="widget-panel.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="widget-panel.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="widget-panel.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="widget-panel.php#top"><i class="fa fa-arrow-up"></i></a>
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
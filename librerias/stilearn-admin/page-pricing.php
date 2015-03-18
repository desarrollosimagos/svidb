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
                    <a href="page-pricing.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="page-pricing.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="page-pricing.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="page-pricing.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="page-pricing.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="page-pricing.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="page-pricing.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="page-pricing.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="page-pricing.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="page-pricing.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="page-pricing.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="page-pricing.php#">
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
                            <a class="view-all" tabindex="-1" href="page-pricing.php#">
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
                        <a href="page-pricing.php#">
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
                        <a href="page-pricing.php#">
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
                        <a href="page-pricing.php#">
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
                        <a href="page-pricing.php#">
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
                        <a href="page-pricing.php#" data-pjax=".content-body">
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
                        <a href="page-pricing.php#" data-pjax=".content-body">
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
                        <a href="page-pricing.php#">
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
                        <a class="item-ch-extra" href="page-pricing.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="page-pricing.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="page-pricing.php#">
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
                            <a href="page-pricing.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="page-pricing.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="page-pricing.php#">Some Action</a></li>
                                <li><a href="page-pricing.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="page-pricing.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="page-pricing.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="page-pricing.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- PAGE PRICING
                    ====================== -->
                    <div class="callout callout-success">
                    	<h4>Lets Play with Pricing Table</h4>
                    	<p>You can make a tons combinations of pricing, just with basic css on the existing theme.</p>
                    </div>
					
					<div class="page-header no-border">
						<h2 class="text-lead">White Angel</h2>
					</div>
                    <div class="row">
                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">STARTED</h2>
                    			</div><!--/as pricing heading-->

                    			<div class="panel-helper-block bg-cloud">
                					<h3 class="text-center">FREE</h3>
                				</div><!--/as pricing price-->

                				<ul class="list-group bordered-bottom">
                    				<li class="list-group-item text-center">1 Website</li>
                    				<li class="list-group-item text-center">Standard Support</li>
                    				<li class="list-group-item text-center">1 Developer</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Source Code</li>
                    				<li class="list-group-item text-center">Include Basic UI</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Subscription</li>
                    			</ul><!--/as pricing feature-->

                    			<div class="panel-body text-center">
                    				<a href="page-pricing.php#" class="btn btn-lg btn-rounded btn-default">PURCHASE</a>
                    			</div><!--/as pricing footer-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">BASIC</h2>
                    			</div><!--/as pricing heading-->

                    			<div class="panel-helper-block bg-cloud">
                					<h3 class="text-center">$10/<span class="text-sm">Month</span></h3>
                				</div><!--/as pricing price-->

                				<ul class="list-group bordered-bottom">
                    				<li class="list-group-item text-center">1 Website</li>
                    				<li class="list-group-item text-center">Standard Support</li>
                    				<li class="list-group-item text-center">1 Developer</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Source Code</li>
                    				<li class="list-group-item text-center">Include All UI</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Subscription</li>
                    			</ul><!--/as pricing feature-->

                    			<div class="panel-body text-center">
                    				<a href="page-pricing.php#" class="btn btn-lg btn-rounded btn-default">PURCHASE</a>
                    			</div><!--/as pricing footer-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-default float-shadow" style="width:100%">
                    			<div class="panel-body text-center bg-inverse">
                    				<h2 class="text-lead text-ellipsis">PROFESSIONAL</h2>
                    			</div><!--/as pricing heading-->

                    			<div class="panel-helper-block bg-primary">
                					<h3 class="text-center">$49/<span class="text-sm">Month</span></h3>
                				</div><!--/as pricing price-->

                				<ul class="list-group bordered-bottom">
                    				<li class="list-group-item text-center">Unlimited Website</li>
                    				<li class="list-group-item text-center">Standard Support</li>
                    				<li class="list-group-item text-center">1 Developer</li>
                    				<li class="list-group-item text-center"><strong>Full</strong> Source Code</li>
                    				<li class="list-group-item text-center">Include All UI</li>
                    				<li class="list-group-item text-center"><strong>Full</strong> Subscription</li>
                    			</ul><!--/as pricing feature-->

                    			<div class="panel-body text-center">
                    				<a href="page-pricing.php#" class="btn btn-lg btn-rounded btn-primary">PURCHASE</a>
                    			</div><!--/as pricing footer-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">BUSINESS</h2>
                    			</div><!--/as pricing heading-->

                    			<div class="panel-helper-block bg-cloud">
                					<h3 class="text-center">$99/<span class="text-sm">Month</span></h3>
                				</div><!--/as pricing price-->

                				<ul class="list-group bordered-bottom">
                    				<li class="list-group-item text-center">Unlimited Website</li>
                    				<li class="list-group-item text-center">Standard Support</li>
                    				<li class="list-group-item text-center">Unlimited Developer</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Source Code</li>
                    				<li class="list-group-item text-center">Include Basic UI</li>
                    				<li class="list-group-item text-center"><strong>No</strong> Subscription</li>
                    			</ul><!--/as pricing feature-->

                    			<div class="panel-body text-center">
                    				<a href="page-pricing.php#" class="btn btn-lg btn-rounded btn-default">PURCHASE</a>
                    			</div><!--/as pricing footer-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->
                    </div><!--/row-->





                    <div class="divider-content">
                    	<span></span>
                    </div><!--/divider-->






                    <div class="page-header no-border">
						<h2 class="text-lead">Minimalize</h2>
					</div>
                    <div class="row">
                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">STARTED</h2>
                					<h4 class="text-center text-muted">FREE</h4>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-cloud text-center">
                					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, doloribus rem sunt debitis excepturi at!</p>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-lg btn-warning">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">BASIC</h2>
                					<h4 class="text-center text-muted">$10/<span class="text-sm">month</span></h4>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-cloud text-center">
                					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, doloribus rem sunt debitis excepturi at!</p>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-lg btn-danger">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-default border-inverse hover">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">PRO</h2>
                					<h4 class="text-center text-muted">$49/<span class="text-sm">month</span></h4>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-inverse text-center">
                					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, doloribus rem sunt debitis excepturi at!</p>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-lg btn-primary">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-default">
                    			<div class="panel-body text-center">
                    				<h2 class="text-lead text-ellipsis">BUSINESS</h2>
                					<h4 class="text-center text-muted">$99/<span class="text-sm">month</span></h4>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-cloud text-center">
                					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, doloribus rem sunt debitis excepturi at!</p>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-lg btn-success">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->
                    </div><!--/row-->


                    <div class="divider-content">
                    	<span></span>
                    </div><!--/divider-->


                    <div class="row">
                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-warning">
                    			<div class="panel-body bg-warning text-center">
                    				<h3 class="text-lead text-ellipsis">STARTED</h3>
                					<p class="text-center text-48">FREE</p>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-white text-center">
                					<ul class="list-percentages row">
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>100 GB</strong></div>
                							<div class="text-muted">DISK SPACE</div>
                						</li>
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>2 TB</strong></div>
                							<div class="text-muted">BANDWIDTH</div>
                						</li>
                					</ul>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-warning">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-danger">
                    			<div class="panel-body bg-danger text-center">
                    				<h3 class="text-lead text-ellipsis">BASIC</h3>
                					<p class="text-center text-48"><sup class="text-32">$</sup>10<span class="text-12"> /month</span></p>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-white text-center">
                					<ul class="list-percentages row">
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>250 GB</strong></div>
                							<div class="text-muted">DISK SPACE</div>
                						</li>
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>4 TB</strong></div>
                							<div class="text-muted">BANDWIDTH</div>
                						</li>
                					</ul>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-danger">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-primary">
                    			<div class="panel-body bg-primary text-center">
                    				<h3 class="text-lead text-ellipsis">PROFESSIONAL</h3>
                					<p class="text-center text-48"><sup class="text-32">$</sup>49<span class="text-12"> /month</span></p>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-white text-center">
                					<ul class="list-percentages row">
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>500 GB</strong></div>
                							<div class="text-muted">DISK SPACE</div>
                						</li>
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>8 TB</strong></div>
                							<div class="text-muted">BANDWIDTH</div>
                						</li>
                					</ul>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-primary">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-3 col-sm-6">
                    		<div class="panel panel-animated panel-success">
                    			<div class="panel-body bg-success text-center">
                    				<h3 class="text-lead text-ellipsis">BUSINESS</h3>
                					<p class="text-center text-48"><sup class="text-32">$</sup>99<span class="text-12"> /month</span></p>
                    			</div><!--/as pricing heading-->

                				<div class="panel-footer bg-white text-center">
                					<ul class="list-percentages row">
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>Unlimited</strong></div>
                							<div class="text-muted">DISK SPACE</div>
                						</li>
                						<li class="col-xs-6">
                							<div class="text-lg"><strong>Unlimited</strong></div>
                							<div class="text-muted">BANDWIDTH</div>
                						</li>
                					</ul>
                    				<p class="helper-block">
                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-success">PURCHASE</a>
                    				</p>
                    			</div><!--/as pricing body-->
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->
                    </div><!--/row-->


                    <div class="divider-content">
                    	<span></span>
                    </div><!--/divider-->
                    

                    <div class="row">
                    	<div class="col-md-6">
                    		<div class="panel panel-animated panel-inverse no-border no-shadow">
                				<ul class="row">
            						<li class="col-xs-4 helper-block-sm absolute-center bg-warning">
            							<div class="absolute-center-item text-center">
            								<h3 class="text-lead text-ellipsis">STARTED</h3>
            								<p class="text-center text-32">FREE</p>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item text-center">
	            							<div class="helper-block margin-bottom">
            									<div class="text-bold text-24">100 GB</div>
            									<div class="text-muted">DISK SPACE</div>
	            							</div>
	            							<div class="helper-block">
	            								<div class="text-bold text-24">2 GB</div>
            									<div class="text-muted">BANDWIDTH</div>
	            							</div>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item" style="width:100%">
	            							<p class="helper-block margin-left margin-right">
		                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-rounded btn-warning">PURCHASE</a>
		                    				</p>
            							</div>
            						</li>
            					</ul>
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-6">
                    		<div class="panel panel-animated panel-inverse no-border no-shadow">
                				<ul class="row">
            						<li class="col-xs-4 helper-block-sm absolute-center bg-danger">
            							<div class="absolute-center-item text-center">
            								<h3 class="text-lead text-ellipsis">BASIC</h3>
            								<p class="text-center text-48"><sup class="text-32">$</sup>10</p>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item text-center">
	            							<div class="helper-block margin-bottom">
            									<div class="text-bold text-24">25 GB</div>
            									<div class="text-muted">DISK SPACE</div>
	            							</div>
	            							<div class="helper-block">
	            								<div class="text-bold text-24">4 GB</div>
            									<div class="text-muted">BANDWIDTH</div>
	            							</div>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item" style="width:100%">
	            							<p class="helper-block margin-left margin-right">
		                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-rounded btn-danger">PURCHASE</a>
		                    				</p>
            							</div>
            						</li>
            					</ul>
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-6">
                    		<div class="panel panel-animated panel-inverse no-border no-shadow">
                				<ul class="row">
            						<li class="col-xs-4 helper-block-sm absolute-center bg-inverse">
            							<div class="absolute-center-item text-center">
            								<h3 class="text-lead text-ellipsis">PROFESSIONAL</h3>
            								<p class="text-center text-48"><sup class="text-32">$</sup>49</p>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-primary">
            							<div class="absolute-center-item text-center">
	            							<div class="helper-block margin-bottom">
            									<div class="text-bold text-24">500 GB</div>
            									<div>DISK SPACE</div>
	            							</div>
	            							<div class="helper-block">
	            								<div class="text-bold text-24">8 GB</div>
            									<div>BANDWIDTH</div>
	            							</div>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-primary">
            							<div class="absolute-center-item" style="width:100%">
	            							<p class="helper-block margin-left margin-right">
		                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-rounded btn-transparent">PURCHASE</a>
		                    				</p>
            							</div>
            						</li>
            					</ul>
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->

                    	<div class="col-md-6">
                    		<div class="panel panel-animated panel-inverse no-border no-shadow">
                				<ul class="row">
            						<li class="col-xs-4 helper-block-sm absolute-center bg-success">
            							<div class="absolute-center-item text-center">
            								<h3 class="text-lead text-ellipsis">BUSINESS</h3>
            								<p class="text-center text-48"><sup class="text-32">$</sup>99</p>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item text-center">
	            							<div class="helper-block margin-bottom">
            									<div class="text-bold text-24">Unlimited</div>
            									<div class="text-muted">DISK SPACE</div>
	            							</div>
	            							<div class="helper-block">
	            								<div class="text-bold text-24">Unlimited</div>
            									<div class="text-muted">BANDWIDTH</div>
	            							</div>
            							</div>
            						</li>
            						<li class="col-xs-4 helper-block-sm absolute-center bg-cloud">
            							<div class="absolute-center-item" style="width:100%">
	            							<p class="helper-block margin-left margin-right">
		                    					<a href="page-pricing.php#" class="btn btn-block btn-lg btn-rounded btn-success">PURCHASE</a>
		                    				</p>
            							</div>
            						</li>
            					</ul>
                    		</div><!--/as pricing table-->
                    	</div><!--/cols-->
                    </div><!--/row-->


                    


                    <div class="divider-content">
                    	<span></span>
                    </div><!--/divider-->



                    
					<div class="page-header no-border">
						<h2 class="text-lead">Presented All The Features of The Product</h2>
					</div>
                    <div class="row">
                    	<div class="col-md-8">
                    		<div class="row">
                    			<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-bar-chart-o text-64 text-primary"></i>
		            					</p>
		            					<p class="text-ellipsis">Realtime Report</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-bar-chart-o text-64 text-primary"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Realtime Report</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-volume-up text-64 text-success"></i>
		            					</p>
		            					<p class="text-ellipsis">Global Marketing</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-volume-up text-64 text-success"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Global Marketing</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-user-md text-64 text-info"></i>
		            					</p>
		            					<p class="text-ellipsis">Full Support</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-user-md text-64 text-info"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Full Support</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-medkit text-64 text-warning"></i>
		            					</p>
		            					<p class="text-ellipsis">30 Days Warranty</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-medkit text-64 text-warning"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">30 Days Warranty</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-clock-o text-64 text-warning"></i>
		            					</p>
		            					<p class="text-ellipsis">Interactive Dashboard</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-clock-o text-64 text-warning"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Interactive Dashboard</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-tasks text-64 text-info"></i>
		            					</p>
		            					<p class="text-ellipsis">Tasks Management</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-tasks text-64 text-info"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Tasks Management</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-heart text-64 text-danger"></i>
		            					</p>
		            					<p class="text-ellipsis">Made with Love</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-heart text-64 text-danger"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Made with Love</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->

		                    	<div class="col-md-3 col-sm-6">
		                    		<div class="hidden-sm hidden-xs box no-border no-shadow text-center bg-cloud">
		            					<p class="float-shadow">
		            						<i class="fa fa-mobile-phone text-64 text-success"></i>
		            					</p>
		            					<p class="text-ellipsis">Responsive Design</p>
		                    		</div><!--/as feature item-->

		                    		<div class="hidden-lg hidden-md box no-border no-shadow text-center bg-cloud">
		                    			<ul class="row">
		            						<li class="col-xs-3 col-md-4 helper-block-xs absolute-center">
		            							<div class="absolute-center-item">
		            								<p class="float-shadow">
		            									<i class="fa fa-mobile-phone text-64 text-success"></i>
		            								</p>
		            							</div>
		            						</li>
		            						<li class="col-xs-9 col-md-8 helper-block-xs absolute-center">
		            							<div class="absolute-center-item" style="width:100%">
			            							<p class="text-left text-ellipsis lead">Responsive Design</p>
		            							</div>
		            						</li>
		            					</ul>
		                    		</div><!--/as feature item-->
		                    	</div><!--/cols-->
                    		</div><!--/row-->

                    	</div><!--/cols-->

                    	<div class="col-md-4">
                    		<div id="carousel-text" class="carousel slide wow fadeInRight" data-ride="carousel">
								<ol class="carousel-indicators">
									<li data-target="#carousel-text" data-slide-to="0" class="active"></li>
									<li data-target="#carousel-text" data-slide-to="1"></li>
									<li data-target="#carousel-text" data-slide-to="2"></li>
								</ol>
								<div class="carousel-inner">
									<div class="item active">
										<div class="jumbotron bg-primary no-margin" style="height:275px">
											<blockquote class="no-border">
											    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut, quam!</p>
											    <small class="text-cloud">Someone famous in <cite title="Source Title">Source Title</cite></small>
											</blockquote>
										</div>
									</div><!--/items-->
									<div class="item">
										<div class="jumbotron bg-inverse no-margin clearfix" style="height:275px">
											<blockquote class="no-border pull-right">
											    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Odit, temporibus?</p>
											    <small class="text-cloud">Someone famous in <cite title="Source Title">Source Title</cite></small>
											</blockquote>
										</div>
									</div><!--/items-->
									<div class="item">
										<div class="jumbotron bg-danger no-margin" style="height:275px">
											<blockquote class="no-border">
											    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque, at?</p>
											    <small class="text-cloud">Someone famous in <cite title="Source Title">Source Title</cite></small>
											</blockquote>
										</div>
									</div><!--/items-->
								</div><!--/carousel-inner-->

								<a class="left carousel-control" href="page-pricing.php#carousel-text" data-slide="prev">
									<span class="glyphicon glyphicon-chevron-left"></span>
								</a>
								<a class="right carousel-control" href="page-pricing.php#carousel-text" data-slide="next">
									<span class="glyphicon glyphicon-chevron-right"></span>
								</a>
							</div><!--/carousel-->
                    	</div><!--/cols-->
                	</div><!--/row-->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="page-pricing.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="page-pricing.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="page-pricing.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="page-pricing.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="page-pricing.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="page-pricing.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="page-pricing.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="page-pricing.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="page-pricing.php#top"><i class="fa fa-arrow-up"></i></a>
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
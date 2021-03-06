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
                    <a href="index.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="index.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="index.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="index.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="index.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="index.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="index.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="index.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="index.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="index.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="index.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="index.php#">
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
                            <a class="view-all" tabindex="-1" href="index.php#">
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
                        <a href="index.php#">
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
                        <a href="index.php#">
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
                        <a href="index.php#">
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
                        <a href="index.php#">
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
                        <a href="index.php#" data-pjax=".content-body">
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
                        <a href="index.php#" data-pjax=".content-body">
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
                        <a href="index.php#">
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
                        <a class="item-ch-extra" href="index.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="index.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="index.php#">
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
                            <a href="index.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="index.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="index.php#">Some Action</a></li>
                                <li><a href="index.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="index.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="index.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="index.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- DASHBOARD
                    ================================================== -->
                    <!-- Dashboard  -->
                    <div id="error-placement"></div>
                    <div class="row margin-top">
                        <div class="col-md-12 margin-bottom">
                            <ul class="nav nav-tabs">
                                <li class="active"><a href="index.php#system-stats" data-toggle="tab">System Stats</a></li>
                                <li><a href="index.php#server-stats" data-toggle="tab">Server Stats</a></li>
                            </ul>
                        </div>

                        <!-- Tab panes -->
                        <div class="tab-content">
                            <div id="system-stats" class="tab-pane fade active in">
                                <div class="col-md-4">
                                    <div id="overall-visitor" class="panel panel-animated panel-primary bg-primary">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-visitor" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to system stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Visitor</p><!--/lead as title-->

                                            <ul class="list-percentages row">
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Monthly</p>
                                                    <p class="text-lg"><strong>765,298</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Weekly</p>
                                                    <p class="text-lg"><strong>1,765</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Today</p>
                                                    <p class="text-lg"><strong>563</strong></p>
                                                </li>
                                            </ul><!--/list-percentages-->
                                            <p class="helper-block">
                                                <div class="progress progress-xs progress-flat progress-inverse-inverse">
                                                    <div class="progress-bar progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                        <span class="sr-only">60% Complete (inverse)</span>
                                                    </div>
                                                </div>
                                                </p><p class="text-ellipsis"><i class="fa fa-caret-up"></i> 654 &nbsp;&nbsp; +21<sup>%</sup> <small>Looks Good!, up from last month</small></p>
                                            <!--/help-block-->
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-visitor-->
                                </div><!--/cols-->

                                <div class="col-md-4">
                                    <div id="overall-users" class="panel panel-animated panel-success bg-success">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-users" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to system stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Users</p><!--/lead as title-->

                                            <ul class="list-percentages row">
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">All Users</p>
                                                    <p class="text-lg"><strong>1437</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Last Month</p>
                                                    <p class="text-lg"><strong>287</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">New Users</p>
                                                    <p class="text-lg"><strong>87</strong></p>
                                                </li>
                                            </ul><!--/list-percentages-->
                                            <p class="helper-block">
                                                <div class="progress progress-xs progress-flat progress-inverse-inverse">
                                                    <div class="progress-bar progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                        <span class="sr-only">60% Complete (inverse)</span>
                                                    </div>
                                                </div>
                                                </p><p class="text-ellipsis"><i class="fa fa-caret-up"></i> 63 &nbsp;&nbsp; +8<sup>%</sup> <small>Looks Good!, up from last month</small></p>
                                            <!--/help-block-->
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-users-->
                                </div><!--/cols-->

                                <div class="col-md-4">
                                    <div id="overall-orders" class="panel panel-animated panel-danger bg-danger">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-orders" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to system stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Orders</p><!--/lead as title-->

                                            <ul class="list-percentages row">
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Total Revenue</p>
                                                    <p class="text-lg"><strong>1,954,452</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Last Month</p>
                                                    <p class="text-lg"><strong>43,671</strong></p>
                                                </li>
                                                <li class="col-xs-4">
                                                    <p class="text-ellipsis">Today</p>
                                                    <p class="text-lg"><strong>1,219</strong></p>
                                                </li>
                                            </ul><!--/list-percentages-->
                                            <p class="helper-block">
                                                <div class="progress progress-xs progress-flat progress-inverse-inverse">
                                                    <div class="progress-bar progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                                        <span class="sr-only">60% Complete (inverse)</span>
                                                    </div>
                                                </div>
                                                </p><p class="text-ellipsis"><i class="fa fa-caret-down"></i> 386 &nbsp;&nbsp; -5<sup>%</sup> <small>Looks not good! try increasing your product</small></p>
                                            <!--/help-block-->
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-orders-->
                                </div><!--/cols-->
                            </div><!--/#system-stats-->


                            <div id="server-stats" class="tab-pane fade">
                                <div class="col-md-4">
                                    <div id="overall-bandwidth" class="panel panel-animated panel-primary bg-primary">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-bandwidth" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to server stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Bandwidth</p><!--/lead as title-->

                                            <p>
                                                <div class="easyPieChart" data-barcolor="#232332" data-trackcolor="#ecf0f1" data-scalecolor="#ecf0f1" data-percent="16" data-size="120">
                                                    <span>16%</span>
                                                </div>
                                                </p><p class="text-ellipsis text-center">Bandwidth Usage 120,4 GB / 2 TB</p>
                                            
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-bandwidth-->
                                </div><!--/cols-->

                                <div class="col-md-4">
                                    <div id="overall-diskspace" class="panel panel-animated panel-success bg-success">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-diskspace" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to server stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Disk Space</p><!--/lead as title-->

                                            <p>
                                                <div class="easyPieChart" data-barcolor="#232332" data-trackcolor="#ecf0f1" data-scalecolor="#ecf0f1" data-percent="37" data-size="120">
                                                    <span>64%</span>
                                                </div>
                                                </p><p class="text-ellipsis text-center">File Usage 128,137 / 200,000</p>
                                            
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-diskspace-->
                                </div><!--/cols-->

                                <div class="col-md-4">
                                    <div id="overall-phisicmem" class="panel panel-animated panel-danger bg-danger">
                                        <div class="panel-body">
                                            <div class="panel-actions-fly">
                                                <button data-refresh="#overall-phisicmem" data-error-place="#error-placement" title="refresh" class="btn-panel">
                                                    <i class="glyphicon glyphicon-refresh"></i>
                                                </button><!--/btn-panel-->
                                                <a href="index.php#" title="Go to server stats page" class="btn-panel">
                                                    <i class="glyphicon glyphicon-stats"></i>
                                                </a><!--/btn-panel-->
                                            </div><!--/panel-action-fly-->

                                            <p class="lead">Physical Memory</p><!--/lead as title-->

                                            <p>
                                                <div class="easyPieChart" data-barcolor="#232332" data-trackcolor="#ecf0f1" data-scalecolor="#ecf0f1" data-percent="45" data-size="120">
                                                    <span>45%</span>
                                                </div>
                                                </p><p class="text-ellipsis text-center">Physical Memory Usage 457 MB / 1 GB</p>
                                            
                                        </div><!--/panel-body-->
                                    </div><!--/panel overal-phisicmem-->
                                </div><!--/cols-->
                            </div><!--/#system-stats-->
                        </div><!--/tab-content-->
                    </div><!--/row-->





                    <div class="row">
                        <div class="col-sm-8">
                            <!-- VMAP -->
                            <div class="panel panel-animated panel-default">
                                <div class="panel-heading bg-white">
                                    <div class="panel-actions">
                                        <div class="btn-group">
                                            <button class="btn-panel dropdown-toggle" data-toggle="dropdown">
                                                Change Maps
                                                <i class="fa fa-angle-down"></i>
                                            </button>
                                            <ul id="changeMapRegion" class="dropdown-menu pull-right">
                                                <li class="active"><a href="index.php#" data-map="world_en">World</a></li>
                                                <li class="divider"></li>
                                                <li><a href="index.php#" data-map="africa_en">Africa</a></li>
                                                <li><a href="index.php#" data-map="asia_en">Asia</a></li>
                                                <li><a href="index.php#" data-map="australia_en">Australia</a></li>
                                                <li><a href="index.php#" data-map="europe_en">Europe</a></li>
                                                <li><a href="index.php#" data-map="north-america_en">North America</a></li>
                                                <li><a href="index.php#" data-map="south-america_en">South America</a></li>
                                                <li class="divider"></li>
                                                <li><a href="index.php#" data-map="dz_fr">Algeria</a></li>
                                                <li><a href="index.php#" data-map="france_fr">France</a></li>
                                                <li><a href="index.php#" data-map="germany_en">Germany</a></li>
                                                <li><a href="index.php#" data-map="russia_en">Russia</a></li>
                                                <li><a href="index.php#" data-map="usa_en">USA</a></li>
                                            </ul>
                                        </div><!--/btn-group-->
                                    </div><!-- /panel-actions -->
                                    <h4 class="panel-title" data-ariginal-title="World Map" id="mapRegion">World Map</h4>
                                </div><!--/panel-heading-->

                                <div class="panel-body">
                                    <div id="vmap" class="vmap" style="height:370px"></div>
                                </div><!--/panel-body-->
                                
                                <ul class="list-group">
                                    <li class="list-group-item" id="legend-region">Summary of World</li>
                                    <li class="list-group-item"><div id="legend-visit" class="badge badge-primary"></div><i class="fa fa-signal"></i> Today Visitor</li>
                                    <li class="list-group-item"><div id="legend-member" class="badge badge-primary"></div><i class="fa fa-users"></i> Members</li>
                                    <li class="list-group-item"><div id="legend-customer" class="badge badge-primary"></div><i class="fa fa-briefcase"></i> Customers</li>
                                    <li class="list-group-item"><div id="legend-online" class="badge badge-primary"></div><i class="fa fa-circle"></i> Online</li>
                                    <li class="list-group-item"><div id="legend-revenue" class="badge badge-primary"></div><i class="fa fa-dollar"></i> Total Revenue</li>
                                </ul><!--/list-group map-legend-->
                            </div><!--/panel-->
                        </div><!--/cols-->


                        <div class="col-sm-4">
                            <div class="panel panel-animated panel-inverse bg-inverse">
                                <div class="panel-body">
                                    <p class="text-lg"><span class="pull-right">64<sup>%</sup></span><i class="fa fa-cloud-download"></i> Downloading...</p>
                                    <div class="progress progress-lg">
                                        <div class="progress-bar progress-bar-inverse" role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" style="width: 64%">
                                            <span class="sr-only">64% Complete (inverse)</span>
                                        </div>
                                    </div>

                                    <p class="text-lg"><span class="pull-right">37<sup>%</sup></span><i class="fa fa-cloud-upload"></i> Uploading...</p>
                                    <div class="progress progress-lg">
                                        <div class="progress-bar progress-bar-inverse" role="progressbar" aria-valuenow="37" aria-valuemin="0" aria-valuemax="100" style="width: 37%">
                                            <span class="sr-only">37% Complete (inverse)</span>
                                        </div>
                                    </div>
                                </div><!--/panel-body-->
                            </div><!--/panel-->


                            <div id="dashboard-weather" class="panel panel-animated panel-default bg-danger border-danger border-danger">
                                <div class="panel-heading bg-transparent no-border">
                                    <h3 class="text-center">Whashington (WA)</h3>
                                </div><!--/panel-heading-->

                                <div class="panel-body text-center bordered-bottom border-transparent">
                                    <p class="text-lg">SAT 08/02</p>
                                    <p class="text-64">23&deg; <canvas id="skycons-wind1" width="64" height="64"></canvas></p>
                                </div><!--/panel-body-->

                                <div class="list-group bg-danger">
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-sun" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">29&deg;</div>
                                        SUN 02/02
                                    </a>
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-snow" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">15&deg;</div>
                                        MON 03/02
                                    </a>
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-cloudy" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">26&deg;</div>
                                        TUE 04/02
                                    </a>
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-wind2" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">24&deg;</div>
                                        WED 05/02
                                    </a>
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-rain" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">22&deg;</div>
                                        THU 06/02
                                    </a>
                                    <a class="list-group-item" href="index.php#">
                                        <canvas class="pull-right" id="skycons-fog" width="16" height="16"></canvas>
                                        <div class="list-group-item-text pull-right">25&deg;</div>
                                        FRI 07/02
                                    </a>
                                </div><!--/list-group-->
                            </div><!--panel-->
                        </div><!--/cols-->
                    </div><!--/row-->





                    <div class="row">
                        <div class="col-md-6">
                            <form action="index.php" role="form">
                            <div class="panel panel-animated panel-default">
                                <div class="panel-heading bg-white">
                                    <h4 class="panel-title"><i class="fa fa-envelope-o"></i> Quick Mail</h4>
                                </div><!--panel-heading-->

                                <div class="panel-body">
                                    <div class="form-group">
                                        <label class="control-label" for="quick-mail-reseiver">To</label>
                                        <input id="quick-mail-reseiver" name="quick-mail-reseiver" type="text" data-input="tags">
                                    </div>
                                    <div class="form-group">
                                        <label class="control-label" for="quick-mail-subject">Subject</label>
                                        <input id="quick-mail-subject" name="quick-mail-subject" type="text" class="form-control">
                                    </div>
                                    <div class="form-group">
                                        <textarea id="quick-mail-content" name="quick-mail-content" class="form-control" data-input="wysihtml5" data-link="false" data-image="false" style="width:100%" rows="12" placeholder="Enter your message ..."></textarea>
                                    </div><!-- /form-group -->
                                </div><!--panel-body-->

                                <div class="panel-footer bg-white bordered-top clearfix">
                                    <div class="pull-right">
                                        <input type="reset" class="btn btn-sm btn-default" value="Cancel">
                                        <input type="submit" class="btn btn-sm btn-inverse" value="Send Email">
                                    </div>
                                </div><!--panel-footer-->
                            </div><!--panel-->
                            </form>
                        </div><!--/cols-->

                        <div class="col-md-6">
                            <div class="panel panel-animated panel-default">
                                <div class="panel-heading bg-white">
                                    <div class="panel-actions">
                                        <button id="calendar-viewtoday" class="btn-panel">Today</button>
                                        <button id="calendar-viewmonth" class="btn-panel active">Month</button>
                                        <button id="calendar-viewweek" class="btn-panel">Week</button>
                                        <button id="calendar-viewday" class="btn-panel">Day</button>
                                    </div><!--panel-actions-->
                                    <h4 class="panel-title" id="calendar-viewtitle"><i class="fa fa-spinner fa-spin"></i></h4>
                                </div><!--panel-heading-->

                                <div class="panel-helper-block">
                                    <div class="btn-toolbar" role="toolbar">
                                        <div class="btn-group btn-group-sm pull-right">
                                            <button class="btn btn-default" id="calendar-viewnext">Next</button>
                                            <button class="btn btn-default" id="calendar-viewnextYear">Next Year</button>
                                        </div>
                                        <div class="btn-group btn-group-sm pull-left">
                                            <button class="btn btn-default" id="calendar-viewprevYear">Prev Year</button>
                                            <button class="btn btn-default" id="calendar-viewprev">Prev</button>
                                        </div>
                                    </div>
                                </div><!--/panel-helper-block-->

                                <div class="panel-body">
                                    <div id="calendar" class="table-responsive calendar-inverse"></div>
                                </div><!--panel-body-->
                            </div><!--panel-->
                        </div><!--/cols-->
                    </div><!--/row-->


                    
                    <div class="divider-content">
                        <span></span>
                    </div><!--/divider-content-->


                    
                    <div id="error-placement2"></div>
                    <div class="page-header no-border">
                    	<h3><i class="fa fa-rss"></i> Content Feeds</h3>
                    </div>
                    <div class="row">
                        <div class="col-md-4">
                            <div id="contentfeeds1" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds1" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds1" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="no-padding jumbotron bg-inverse">
                                        <div class="tile">
                                            <div class="img-wrapper">
                                                <img class="lazy" data-original="images/dummy/2590d12d.img2.png" alt="">
                                            </div>
                                        </div>
                                        
                                        <div class="jumbotron-text">
                                            <p class="lead">The Ideas to Become a Creative Professionals</p>
                                            <p class="clearfix">
                                                <span class="pull-right">
                                                    <a href="index.php#" class="btn btn-xs btn-inverse btn-rounded">#webDesign</a>
                                                    <a href="index.php#" class="btn btn-xs btn-inverse btn-rounded">#beginner</a>
                                                </span>
                                            </p>
                                        </div>
                                    </div><!--/jumbotron-->

                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/f5a2c818.uifaces14.jpg" alt="uifaces14" width="46px" width="46px">
                                        <div class="text-14"><strong>Kathy Reynolds</strong></div>
                                        <div class="text-muted"><small>Share Public Post - a hours ago</small></div>
                                    </div><!--/profile-line-->

                                    <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, dolores facilis maiores minus itaque excepturi.</p>
                                    
                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 21 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 16</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->



                            <div id="contentfeeds4" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds4" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds4" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="no-padding jumbotron bg-primary">
                                        <p class="lead">The 20 best Google Chrome extensions for web designers</p>
                                        <p class="clearfix">
                                            <span class="pull-right">
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#chrome</a>
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#tools</a>
                                            </span>
                                        </p>
                                    </div><!--/jumbotron-->

                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/9c06e6a0.uifaces11.jpg" alt="uifaces11" width="46px" width="46px">
                                        <div class="text-14"><strong>Samantha Jenkins</strong></div>
                                        <div class="text-muted"><small>Share Public Post - Yesterday</small></div>
                                    </div><!--/profile-line-->

                                    <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, dolores facilis maiores minus itaque excepturi.</p>
                                    
                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 34 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 51</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="pull-left margin-right">
                                            <img class="img-circle" src="images/dummy/0c31c9dc.profile.jpg" alt="profile" width="36px" width="36px">
                                        </div>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->
                        </div><!--/cols-->


                        <div class="col-md-4">
                            <div id="contentfeeds2" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds2" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds2" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/e9d19848.uifaces19.jpg" alt="uifaces19" width="46px" width="46px">
                                        <div class="text-14"><strong>Phillip Morrison</strong></div>
                                        <div class="text-muted"><small>Share Exclusive Post - 7:16 AM</small></div>
                                    </div><!--/profile-line-->

                                    <div class="no-padding jumbotron bg-primary">
                                        <p class="lead">Times Designers Are Monitoring Reaction to the Redesign, With Adjustments Possible</p>
                                        <p class="clearfix">
                                            <span class="pull-right">
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#manage</a>
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#workFlow</a>
                                            </span>
                                        </p>
                                    </div><!--/jumbotron-->

                                    <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, dolores facilis maiores minus itaque excepturi.</p>
                                    
                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 47 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 98</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->

                            <div id="contentfeeds5" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds5" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds5" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="no-padding jumbotron bg-inverse">
                                        <p class="lead">COMPRESSED DATA; Homing In on 'Intelligent' Web Design</p>
                                        <p class="clearfix">
                                            <span class="pull-right">
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#webDesign</a>
                                            </span>
                                        </p>
                                    </div><!--/jumbotron-->

                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/3a93212e.uifaces3.jpg" alt="uifaces3" width="46px" width="46px">
                                        <div class="text-14"><strong>Aaron James</strong></div>
                                        <div class="text-muted"><small>Share Public Post - Yesterday</small></div>
                                    </div><!--/profile-line-->

                                    <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, dolores facilis maiores minus itaque excepturi.</p>
                                    
                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 28 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 31</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->
                        </div><!--/cols-->


                        <div class="col-md-4">
                            <div id="contentfeeds3" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds3" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds3" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="no-padding jumbotron bg-danger">
                                        <p class="lead">Make Your Design Keep Simple and Easy Read</p>
                                        <p class="clearfix">
                                            <span class="pull-right">
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#stilearn</a>
                                                <a href="index.php#" class="btn btn-xs btn-transparent btn-rounded">#clean</a>
                                            </span>
                                        </p>
                                    </div><!--/jumbotron-->

                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/3a93212e.uifaces3.jpg" alt="uifaces3" width="46px" width="46px">
                                        <div class="text-14"><strong>Aaron James</strong></div>
                                        <div class="text-muted"><small>Share Public Post - 6:36 AM</small></div>
                                    </div><!--/profile-line-->

                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 8 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 12</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="pull-left margin-right">
                                            <img class="img-circle" src="images/dummy/0c31c9dc.profile.jpg" alt="profile" width="36px" width="36px">
                                        </div>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->


                            <div id="contentfeeds6" class="panel panel-animated panel-default">
                                <div class="panel-actions-fly">
                                    <button data-refresh="#contentfeeds6" data-error-place="#error-placement2" title="refresh" class="btn-panel">
                                        <i class="fa fa-refresh"></i>
                                    </button><!--/btn-panel-->
                                    <button data-close="#contentfeeds6" title="close" class="btn-panel">
                                        <i class="fa fa-times"></i>
                                    </button><!--/btn-panel-->
                                </div><!--/panel-action-fly-->

                                <div class="panel-body bordered-bottom">
                                    <div class="profile-line clearfix">
                                        <img class="img-circle pull-left" src="images/dummy/8af46bf8.uifaces21.jpg" alt="uifaces21" width="46px" width="46px">
                                        <div class="text-14"><strong>John Doe</strong></div>
                                        <div class="text-muted"><small>Share Exclusive Post - Yesterday</small></div>
                                    </div><!--/profile-line-->

                                    <div class="no-padding jumbotron bg-warning">
                                        <div class="tile">
                                            <div class="img-wrapper">
                                                <img class="lazy" data-original="images/dummy/75ccb40a.img5.png" alt="">
                                            </div>
                                        </div>
                                        <div class="jumbotron-text">
                                            <p class="lead">Technology Tools: Web 2.0 in the Classroom</p>
                                            <p class="clearfix">
                                                <span class="pull-right">
                                                    <a href="index.php#" class="btn btn-xs btn-warning btn-rounded">#tools</a>
                                                    <a href="index.php#" class="btn btn-xs btn-warning btn-rounded">#technology</a>
                                                </span>
                                            </p>
                                        </div>
                                    </div><!--/jumbotron-->

                                    <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, dolores facilis maiores minus itaque excepturi.</p>
                                    
                                    <p class="text-muted pull-right"><i class="fa fa-comment"></i> 87 &nbsp;&nbsp;&nbsp; <i class="fa fa-heart"></i> 163</p>
                                </div><!--panel-body-->

                                <div class="panel-body">
                                    <form action="index.php" role="form">
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" placeholder="Write a comment...">
                                            <span class="input-group-btn">
                                                <span class="fileinput fileinput-new" data-provides="fileinput">
                                                    <button class="btn btn-transparent text-muted btn-file" type="button">
                                                        <i class="fileinput-new fa fa-camera"></i>
                                                        <input type="file" name="fileinput_inline[]">
                                                    </button>
                                                    <button class="btn btn-transparent fileinput-exists text-muted" rel="tooltip-bottom" title="remove file attach" data-dismiss="fileinput"><i class="fa fa-times"></i></button>
                                                </span>
                                            </span>
                                        </div>
                                    </form><!--/form-->
                                </div><!--/panel-body-->
                            </div><!--/panel-->
                        </div><!--/cols-->
                    </div><!--/row-->



                    <div id="content-feeds"></div>
                    <p class="text-center">
                        <a data-ajax="#content-feeds" data-scripts="data-sample/feeds-content.js" href="data-sample/feeds-content.html" data-max-page="5" data-loading-text="<i class='fa fa-spin fa-spinner'></i> Loading..." class="btn btn-sm btn-cloud">Load more feeds...</a>
                    </p>                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="index.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="index.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="index.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="index.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="index.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="index.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="index.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="index.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="index.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="index.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="index.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="index.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="index.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="index.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="index.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="index.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="index.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="index.php#top"><i class="fa fa-arrow-up"></i></a>
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
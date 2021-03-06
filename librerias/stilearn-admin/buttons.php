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
                    <a href="buttons.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="buttons.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="buttons.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="buttons.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="buttons.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="buttons.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="buttons.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="buttons.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="buttons.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="buttons.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="buttons.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="buttons.php#">
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
                            <a class="view-all" tabindex="-1" href="buttons.php#">
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
                        <a href="buttons.php#">
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
                        <a href="buttons.php#">
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
                        <a href="buttons.php#">
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
                        <a href="buttons.php#">
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
                        <a href="buttons.php#" data-pjax=".content-body">
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
                        <a href="buttons.php#" data-pjax=".content-body">
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
                        <a href="buttons.php#">
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
                        <a class="item-ch-extra" href="buttons.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="buttons.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="buttons.php#">
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
                            <a href="buttons.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="buttons.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="buttons.php#">Some Action</a></li>
                                <li><a href="buttons.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="buttons.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="buttons.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="buttons.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- BUTTONS
                    ================================================== -->
                    <div class="page-header">
                        <h1 id="buttons">Buttons & Paginations</h1>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <div id="panel-btndemo" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-btndemo" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-btndemo" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-btndemo" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-btndemo" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Basic Buttons</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p>Use any of the available button classes to quickly create a styled button <code>.btn</code>. Use the button classes on an <code>&lt;a&gt;</code>, <code>&lt;button&gt;</code>, or <code>&lt;input&gt;</code> element. Available class:</p> 
                                    <p><code>.btn-default</code> <code>.btn-inverse</code> <code>.btn-primary</code> <code>.btn-success</code> <code>.btn-info</code> <code>.btn-warning</code> <code>.btn-danger</code> <code>.btn-cloud</code> <code>.btn-silver</code> <code>.btn-link</code></p>
                                    <p class="text-muted"><strong>Options</strong></p>
                                    <button type="button" class="btn btn-default">Default</button>
                                    <button type="button" class="btn btn-inverse">Inverse</button>
                                    <button type="button" class="btn btn-primary">Primary</button>
                                    <button type="button" class="btn btn-success">Success</button>
                                    <button type="button" class="btn btn-info">Info</button>
                                    <button type="button" class="btn btn-warning">Warning</button>
                                    <button type="button" class="btn btn-danger">Danger</button>
                                    <button type="button" class="btn btn-cloud">Cloud</button>
                                    <button type="button" class="btn btn-silver">Silver</button>
                                    <button type="button" class="btn btn-link">Link</button>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Size</strong> <code>.btn-lg .btn-sm .btn-xs</code></p>
                                            <button type="button" class="btn btn-lg btn-default">Default</button>
                                            <button type="button" class="btn btn-inverse">Inverse</button>
                                            <button type="button" class="btn btn-sm btn-primary">Primary</button>
                                            <button type="button" class="btn btn-xs btn-success">Success</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Badge</strong> <code>.btn > .badge</code></p>
                                            <button type="button" class="btn btn-lg btn-default"><span class="badge">5</span> Default</button>
                                            <button type="button" class="btn btn-inverse"><span class="badge">6</span> Inverse</button>
                                            <button type="button" class="btn btn-sm btn-primary"><span class="badge">7</span> Primary</button>
                                            <button type="button" class="btn btn-xs btn-success"><span class="badge">8</span> Success</button>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Icon</strong> <code>.btn > .fa</code></p>
                                            <button type="button" class="btn btn-lg btn-default"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-inverse"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-sm btn-primary"><i class="fa fa-cog"></i> Settings</button>
                                            <button type="button" class="btn btn-xs btn-success"><i class="fa fa-cog"></i> Settings</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Alternative use with icons</strong></p>
                                            <div class="btn-group">
                                                <a class="btn btn-default" href="buttons.php#"><i class="fa fa-user fa-fw"></i> User</a>
                                                <a class="btn btn-default dropdown-toggle" data-toggle="dropdown" href="buttons.php#">
                                                    <span class="fa fa-caret-down"></span>
                                                </a>
                                                <ul class="dropdown-menu">
                                                    <li><a href="buttons.php#"><i class="fa fa-pencil fa-fw"></i> Edit</a></li>
                                                    <li><a href="buttons.php#"><i class="fa fa-trash-o fa-fw"></i> Delete</a></li>
                                                    <li><a href="buttons.php#"><i class="fa fa-ban fa-fw"></i> Ban</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="buttons.php#"><i class="fa fa-sign-out fa-fw"></i> Sign Out</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Active state</strong> <code>.active</code></p>
                                            <button type="button" class="btn active btn-default">Default</button>
                                            <button type="button" class="btn active btn-inverse">Inverse</button>
                                            <button type="button" class="btn active btn-primary">Primary</button>
                                            <button type="button" class="btn active btn-success">Success</button>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Disabled state</strong> <code>disabled=&quot;disabled&quot;</code></p>
                                            <button type="button" class="btn btn-default" disabled="disabled">Default</button>
                                            <button type="button" class="btn btn-inverse" disabled="disabled">Inverse</button>
                                            <button type="button" class="btn btn-primary" disabled="disabled">Primary</button>
                                            <button type="button" class="btn btn-success" disabled="disabled">Success</button>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Rounded</strong> <code>.btn-rounded</code></p>
                                    <p>Best use with single button action, like a <strong>Call Action</strong>.</p>
                                    <button type="button" class="btn btn-rounded btn-lg btn-default">Default</button>
                                    <button type="button" class="btn btn-rounded btn-inverse">Inverse</button>
                                    <button type="button" class="btn btn-rounded btn-sm btn-primary">Primary</button>
                                    <button type="button" class="btn btn-rounded btn-xs btn-success" style="margin-right:20px">Success</button>

                                    <button type="button" class="btn btn-rounded btn-info">Info</button>
                                    <button type="button" class="btn btn-rounded btn-warning">Warning</button>
                                    <button type="button" class="btn btn-rounded btn-danger">Danger</button>
                                    <button type="button" class="btn btn-rounded btn-cloud">Cloud</button>
                                    <button type="button" class="btn btn-rounded btn-silver">Silver</button>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Buttons icon</strong> <code>.btn-icon</code></p>
                                            <p>
                                                <button class="btn btn-icon btn-lg btn-default">
                                                    <i class="fa fa-circle"></i>
                                                    Default
                                                </button>
                                                <button class="btn btn-icon btn-inverse">
                                                    <i class="fa fa-circle-o"></i>
                                                    Inverse
                                                </button>
                                                <button class="btn btn-icon btn-sm btn-primary">
                                                    <i class="fa fa-check"></i>
                                                    Primary
                                                </button>
                                                <button class="btn btn-icon btn-xs btn-danger">
                                                    <i class="fa fa-exclamation"></i>
                                                    Danger
                                                </button>
                                            </p>
                                        </div><!-- /cols -->

                                        <div class="col-md-6">
                                            <p class="text-muted"><strong>Align</strong> <code>.btn-icon.btn-icon-right</code></p>
                                            <p>
                                                <button class="btn btn-icon btn-icon-right btn-xs btn-default">
                                                    <i class="fa fa-circle"></i>
                                                    Default
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-sm btn-inverse">
                                                    <i class="fa fa-circle-o"></i>
                                                    Inverse
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-primary">
                                                    <i class="fa fa-check"></i>
                                                    Primary
                                                </button>
                                                <button class="btn btn-icon btn-icon-right btn-lg btn-danger">
                                                    <i class="fa fa-exclamation"></i>
                                                    Danger
                                                </button>
                                            </p>
                                        </div><!-- /cols -->
                                    </div><!-- /row -->
                                    <br>
                                    <p>
                                        <button type="button" class="btn btn-icon btn-default">
                                            <i class="fa fa-circle"></i>
                                            Default
                                        </button>
                                        <button type="button" class="btn btn-icon btn-inverse">
                                            <i class="fa fa-circle-o"></i>
                                            Inverse
                                        </button>
                                        <button type="button" class="btn btn-icon btn-primary">
                                            <i class="fa fa-check"></i>
                                            Primary
                                        </button>
                                        <button type="button" class="btn btn-icon btn-success">
                                            <i class="fa fa-check-circle"></i>
                                            Success
                                        </button>
                                        <button type="button" class="btn btn-icon btn-info">
                                            <i class="fa fa-info"></i>
                                            Info
                                        </button>
                                        <button type="button" class="btn btn-icon btn-warning">
                                            <i class="fa fa-warning"></i>
                                            Warning
                                        </button>
                                        <button type="button" class="btn btn-icon btn-danger">
                                            <i class="fa fa-exclamation"></i>
                                            Danger
                                        </button>
                                        <button type="button" class="btn btn-icon btn-cloud">
                                            <i class="fa fa-cloud"></i>
                                            Cloud
                                        </button>
                                    </p>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Block level</strong> <code>.btn-block</code></p>
                                    <button type="button" class="btn btn-block btn-lg btn-default">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-inverse">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-primary">Block level button</button>
                                    <button type="button" class="btn btn-block btn-lg btn-success">Block level button</button>
                                </div><!-- /panel-body -->

                            </div><!-- /panel-btndemo -->
                        </div><!-- /cols -->
                    </div><!-- /row -->



                    <div class="row">
                        <div class="col-md-12" data-toggle="sortable-widget">
                            <div id="panel-btngroup" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-btngroup" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-btngroup" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-btngroup" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-btngroup" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title sortable-widget-handle">Button groups & Dropdowns</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p>Group a series of buttons together on a single line with the button group. Add on optional JavaScript radio and checkbox style behavior with <a rel="tooltip" title="Bootstrap buttons plugin" target="_blank" href="http://getbootstrap.com/javascript/#buttons">Bootstrap buttons plugin</a>.</p>
                                    <div class="callout callout-info">
                                        <h4>Tooltips &amp; popovers in button groups require special setting</h4>
                                        <p>When using tooltips or popovers on elements within a <code>.btn-group</code>, you'll have to specify the option <code>container: 'body'</code> to avoid unwanted side effects (such as the element growing wider and/or losing its rounded corners when the tooltip or popover is triggered).</p>
                                    </div>
                                    <p class="text-muted"><strong>Basic</strong></p>
                                    <div class="btn-group btn-group-lg">
                                        <button type="button" class="btn btn-default">Left</button>
                                        <button type="button" class="btn btn-default">Middle</button>
                                        <button type="button" class="btn btn-default">Right</button>
                                    </div>
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Left</button>
                                        <button type="button" class="btn btn-inverse">Middle</button>
                                        <button type="button" class="btn btn-inverse">Right</button>
                                    </div>
                                    <div class="btn-group btn-group-sm">
                                        <button type="button" class="btn btn-primary">Left</button>
                                        <button type="button" class="btn btn-primary">Middle</button>
                                        <button type="button" class="btn btn-primary">Right</button>
                                    </div>
                                    <div class="btn-group btn-group-xs">
                                        <button type="button" class="btn btn-danger">Left</button>
                                        <button type="button" class="btn btn-danger">Middle</button>
                                        <button type="button" class="btn btn-danger">Right</button>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Nesting</strong></p>
                                    <div class="btn-group btn-group-lg">
                                        <button type="button" class="btn btn-default">Left</button>
                                        <button type="button" class="btn btn-default">Right</button>
                                        <div class="btn-group btn-group-lg">
                                            <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Left</button>
                                        <button type="button" class="btn btn-inverse">Right</button>
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group btn-group-sm">
                                        <button type="button" class="btn btn-primary">Left</button>
                                        <button type="button" class="btn btn-primary">Right</button>

                                        <div class="btn-group btn-group-sm">
                                            <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div class="btn-group btn-group-xs">
                                        <button type="button" class="btn btn-danger">Left</button>
                                        <button type="button" class="btn btn-danger">Right</button>
                                        <div class="btn-group btn-group-xs btn-group-xs">
                                            <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </button>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Toolbar</strong></p>
                                    <div class="btn-toolbar" role="toolbar">
                                        <div class="btn-group" data-toggle="buttons">
                                            <button rel="tooltip-bottom" title="bold" class="btn btn-default"><i class="fa fa-bold"></i></button>
                                            <button rel="tooltip-bottom" title="italic" class="btn btn-default"><i class="fa fa-italic"></i></button>
                                            <button rel="tooltip-bottom" title="underline" class="btn btn-default"><i class="fa fa-underline"></i></button>
                                            <button rel="tooltip-bottom" title="strikethrough" class="btn btn-default"><i class="fa fa-strikethrough"></i></button>
                                        </div>
                                        <div class="btn-group">
                                            <button rel="tooltip-bottom" title="list-ol" class="btn btn-default"><i class="fa fa-list-ol"></i></button>
                                            <button rel="tooltip-bottom" title="list-ul" class="btn btn-default"><i class="fa fa-list-ul"></i></button>
                                            <button rel="tooltip-bottom" title="table" class="btn btn-default"><i class="fa fa-table"></i></button>
                                        </div>
                                        <div class="btn-group" data-toggle="buttons">
                                            <button rel="tooltip-bottom" title="align-center" class="btn btn-default"><i class="fa fa-align-center"></i></button>
                                            <button rel="tooltip-bottom" title="align-justify" class="btn btn-default"><i class="fa fa-align-justify"></i></button>
                                            <button rel="tooltip-bottom" title="align-left" class="btn btn-default"><i class="fa fa-align-left"></i></button>
                                            <button rel="tooltip-bottom" title="align-right" class="btn btn-default"><i class="fa fa-align-right"></i></button>
                                        </div>
                                        <button data-refresh="#panel-btngroup" rel="tooltip-bottom" title="refresh" class="btn btn-default"><i class="fa fa-refresh"></i></button>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Justified</strong> <code>.btn-group-justified</code></p>
                                    <div class="callout callout-warning">
                                        <h4>Element-specific usage</h4>
                                        <p>This only works with <code>&lt;a&gt;</code> elements as the <code>&lt;button&gt;</code> doesn't pick up the styles we use to justify content (some <code>display: table-cell;</code>-fu).</p>
                                    </div>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-default">Left</a>
                                        <a role="button" class="btn btn-default">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-inverse">Left</a>
                                        <a role="button" class="btn btn-inverse">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-primary">Left</a>
                                        <a role="button" class="btn btn-primary">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="btn-group btn-group-justified">
                                        <a role="button" class="btn btn-success">Left</a>
                                        <a role="button" class="btn btn-success">Right</a>
                                        <div class="btn-group btn-group-lg">
                                            <a role="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown">
                                            Dropdown
                                            <span class="caret"></span>
                                            </a>
                                            <ul class="dropdown-menu">
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                                <li><a href="buttons.php#">Dropdown link</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Single button dropdowns & animated</strong></p>
                                    <div class="callout callout-danger">
                                        <h4>Plugin dependency</h4>
                                        <p>Button dropdowns require the <a rel="tooltip" title="Dropdown plugin" target="_blank" href="http://getbootstrap.com/javascript/#dropdowns">dropdown plugin</a> to be included in your version of Bootstrap. Support with all of <a rel="tooltip" title="animate.css" target="_blank" href="https://daneden.me/animate/">animate.css</a> (animate in type) by <strong>Dan Eden</strong>.</p>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated flipInX" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated flipInY" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated bounceIn" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                        Action <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu animated fadeInLeft" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Single button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown">
                                        Pull right <i class="fa fa-angle-down"></i>
                                        </button>
                                        <ul class="dropdown-menu pull-right animated fadeInLeft" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Split button dropdowns and dropup variation</strong></p>
                                    <!-- Split button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-default">Action</button>
                                        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-down"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated lightSpeedIn" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-inverse">Action</button>
                                        <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-down"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated rollIn" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group dropup">
                                        <button type="button" class="btn btn-primary">Action</button>
                                        <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-up"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated fadeInUp" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                    <!-- Split button -->
                                    <div class="btn-group dropup">
                                        <button type="button" class="btn btn-danger">Action</button>
                                        <button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown">
                                            <i class="fa fa-angle-up"></i>
                                            <span class="sr-only">Toggle Dropdown</span>
                                        </button>
                                        <ul class="dropdown-menu animated rotateIn" role="menu">
                                            <li><a href="buttons.php#">Action</a></li>
                                            <li><a href="buttons.php#">Another action</a></li>
                                            <li><a href="buttons.php#">Something else here</a></li>
                                            <li class="divider"></li>
                                            <li><a href="buttons.php#">Separated link</a></li>
                                        </ul>
                                    </div>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Playing with icons</strong></p>
                                    <p>
                                        <button class="btn btn-default">
                                            <i class="fa fa-spinner fa-spin"></i>
                                        </button>
                                        <button class="btn btn-inverse">
                                            <i class="fa fa-refresh fa-spin"></i>
                                        </button>
                                        <button class="btn btn-primary" style="margin-right:20px">
                                            <i class="fa fa-cog fa-spin"></i>
                                        </button>

                                        <button class="btn btn-cloud">
                                            <i class="fa fa-github"></i>
                                        </button>
                                        <button class="btn btn-success">
                                            <i class="fa fa-html5"></i>
                                        </button>
                                        <button class="btn btn-info">
                                            <i class="fa fa-twitter"></i>
                                        </button>
                                        <button class="btn btn-warning">
                                            <i class="fa fa-stack-overflow"></i>
                                        </button>
                                        <button class="btn btn-danger">
                                            <i class="fa fa-youtube-play"></i>
                                        </button>
                                        <button class="btn btn-silver">
                                            <i class="fa fa-google-plus"></i>
                                        </button>
                                    </p>
                                    <p>
                                        <a class="btn btn-lg btn-primary" target="_blank" href="https://wrapbootstrap.com/theme/stilearn-admin-template-WB0TFD2S0">
                                            <i class="fa fa-flag fa-3x pull-left"></i> Buy Stilearn Admin<br>Version 2.0
                                        </a>
                                    </p>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-btngroup -->



                

                            <div id="panel-pagination" class="panel panel-default sortable-widget-item">
                                <div class="panel-heading">
                                    <div class="panel-actions">
                                        <button data-refresh="#panel-pagination" title="refresh" class="btn-panel">
                                            <i class="fa fa-refresh"></i>
                                        </button>
                                        <button data-expand="#panel-pagination" title="expand" class="btn-panel">
                                            <i class="fa fa-expand"></i>
                                        </button>
                                        <button data-collapse="#panel-pagination" title="collapse" class="btn-panel">
                                            <i class="fa fa-caret-down"></i>
                                        </button>
                                        <button data-close="#panel-pagination" title="close" class="btn-panel">
                                            <i class="fa fa-times"></i>
                                        </button>
                                    </div><!-- /panel-actions -->
                                    <h3 class="panel-title"><i class="fa fa-bars sortable-widget-handle"></i> Paginations</h3>
                                </div><!-- /panel-heading -->

                                <div class="panel-body bordered-bottom">
                                    <p class="text-muted"><strong>Simple pagination</strong></p>
                                    <p>Fancy larger or smaller pagination? Add .pagination-lg or .pagination-sm for additional sizes.</p>
                                    <ul class="pagination pagination-sm">
                                        <li class="disabled"><a href="buttons.php#">&laquo;</a></li>
                                        <li class="active"><a href="buttons.php#">1</a></li>
                                        <li><a href="buttons.php#">2</a></li>
                                        <li><a href="buttons.php#">3</a></li>
                                        <li><a href="buttons.php#">4</a></li>
                                        <li><a href="buttons.php#">5</a></li>
                                        <li><a href="buttons.php#">&raquo;</a></li>
                                    </ul>
                                    <ul class="pagination">
                                        <li class="disabled"><a href="buttons.php#">&laquo;</a></li>
                                        <li class="active"><a href="buttons.php#">1</a></li>
                                        <li><a href="buttons.php#">2</a></li>
                                        <li><a href="buttons.php#">3</a></li>
                                        <li><a href="buttons.php#">4</a></li>
                                        <li><a href="buttons.php#">5</a></li>
                                        <li><a href="buttons.php#">&raquo;</a></li>
                                    </ul>
                                    <ul class="pagination pagination-lg">
                                        <li class="disabled"><a href="buttons.php#">&laquo;</a></li>
                                        <li class="active"><a href="buttons.php#">1</a></li>
                                        <li><a href="buttons.php#">2</a></li>
                                        <li><a href="buttons.php#">3</a></li>
                                        <li><a href="buttons.php#">4</a></li>
                                        <li><a href="buttons.php#">5</a></li>
                                        <li><a href="buttons.php#">&raquo;</a></li>
                                    </ul>
                                </div><!-- /panel-body -->

                                <div class="panel-body">
                                    <p class="text-muted"><strong>Pager</strong></p>
                                    <p>Quick previous and next links for simple pagination implementations with light markup and styles. It's great for simple sites like blogs or magazines.</p>
                                    <ul class="pager">
                                        <li><a href="buttons.php#">Previous</a></li>
                                        <li><a href="buttons.php#">Next</a></li>
                                    </ul>

                                    <p class="text-muted"><strong>Aligned links</strong></p>
                                    <p>Alternatively, you can align each link to the sides:</p>
                                    <ul class="pager">
                                        <li class="previous"><a href="buttons.php#">&larr; Older</a></li>
                                        <li class="next"><a href="buttons.php#">Newer &rarr;</a></li>
                                    </ul>
                                    <p class="text-muted"><strong>Optional disabled state</strong></p>
                                    <p>Pager links also use the general <code>.disabled</code> utility class from the pagination.</p>
                                    <ul class="pager">
                                        <li class="previous disabled"><a href="buttons.php#">&larr; Older</a></li>
                                        <li class="next"><a href="buttons.php#">Newer &rarr;</a></li>
                                    </ul>
                                </div><!-- /panel-body -->
                            </div><!-- /panel-pagination -->
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
                            <a href="buttons.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="buttons.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="buttons.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="buttons.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="buttons.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="buttons.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="buttons.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="buttons.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="buttons.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="buttons.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="buttons.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="buttons.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="buttons.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="buttons.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="buttons.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="buttons.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="buttons.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="buttons.php#top"><i class="fa fa-arrow-up"></i></a>
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
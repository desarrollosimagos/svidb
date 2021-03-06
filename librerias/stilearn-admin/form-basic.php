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
                    <a href="form-basic.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="form-basic.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="form-basic.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="form-basic.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="form-basic.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="form-basic.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-basic.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="form-basic.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-basic.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="form-basic.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-basic.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-basic.php#">
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
                            <a class="view-all" tabindex="-1" href="form-basic.php#">
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
                        <a href="form-basic.php#">
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
                        <a href="form-basic.php#">
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
                        <a href="form-basic.php#">
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
                        <a href="form-basic.php#">
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
                        <a href="form-basic.php#" data-pjax=".content-body">
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
                        <a href="form-basic.php#" data-pjax=".content-body">
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
                        <a href="form-basic.php#">
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
                        <a class="item-ch-extra" href="form-basic.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="form-basic.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="form-basic.php#">
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
                            <a href="form-basic.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="form-basic.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="form-basic.php#">Some Action</a></li>
                                <li><a href="form-basic.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="form-basic.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="form-basic.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="form-basic.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- BASIC FORM
                    ================================================== -->
                    <!-- BASIC FORM  -->
                    <div id="panel-basicform" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-basicform" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-basicform" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-basicform" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-basicform" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Input Fields</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form class="form-horizontal form-bordered" role="form">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="input">Text Input</label>
                                    <div class="col-sm-5">
                                        <input type="text" class="form-control" id="input" placeholder="Placeholder">
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputDis">Text Disable</label>
                                    <div class="col-sm-5">
                                        <input type="text" class="form-control" id="inputDis" placeholder="Placeholder" disabled="disabled">
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputPass">Password Input</label>
                                    <div class="col-sm-5">
                                        <input type="password" class="form-control" id="inputPass" placeholder="Placeholder">
                                        <span class="help-block">A longer block of help text that breaks onto a new line and may extend beyond one line.</span>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputSelect">Selects</label>
                                    <div class="col-sm-5">
                                        <select class="form-control" id="inputSelect">
                                            <option>- Select One -</option>
                                            <option>1</option>
                                            <option>2</option>
                                            <option>3</option>
                                            <option>4</option>
                                            <option>5</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputMultiple">Multiple</label>
                                    <div class="col-sm-5">
                                        <select class="form-control" id="inputMultiple" multiple="multiple">
                                            <option>1</option>
                                            <option>2</option>
                                            <option>3</option>
                                            <option>4</option>
                                            <option>5</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Static control</label>
                                    <div class="col-sm-5">
                                        <p class="form-control-static">email@example.com</p>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Radios</label>
                                    <div class="col-sm-5">
                                        <!-- Keep using .checkbox for radio, couse bootstrap .radio have any conflict with uniform .radio -->
                                        <div class="checkbox">
                                            <label>
                                                <input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked="checked">
                                                Option one is this and that&mdash;be sure to include why it's great
                                            </label>
                                        </div>
                                        <div class="checkbox">
                                            <label>
                                                <input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">
                                                Option two can be something else and selecting it will deselect option one
                                            </label>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Checkboxes</label>
                                    <div class="col-sm-5">
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" name="checkboxes" value="1" checked="checked"> Option one is this and that
                                            </label>
                                        </div>
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" name="checkboxes" value="2"> Be sure to include why it's great
                                            </label>
                                        </div>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Inline checkboxes</label>
                                    <div class="col-sm-5">
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox1" value="option1" checked="checked"> @bent
                                        </label>
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox2" value="option2"> @Iin
                                        </label>
                                        <label class="checkbox-inline">
                                            <input type="checkbox" id="inlineCheckbox3" value="option3"> @stilearningTwit
                                        </label>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputTextarea">Textarea</label>
                                    <div class="col-sm-5">
                                        <textarea rows="3" class="form-control" id="inputTextarea" placeholder="Placeholder"></textarea>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputAutogrow">Autogrow</label>
                                    <div class="col-sm-5">
                                        <textarea rows="3" class="form-control autogrow" id="inputAutogrow" placeholder="Type any line and I will auto grow"></textarea>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <div class="col-sm-offset-3 col-sm-5">
                                        <button type="submit" class="btn btn-default">Submit Form</button>
                                    </div>
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-basicform -->




                    <div id="panel-rpcdefault" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-rpcdefault" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-rpcdefault" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-rpcdefault" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-rpcdefault" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Replaced default style</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Checkbox</strong></p>
                                            <p>Just give you a nice custom Checkbox style with pure CSS and Font Awesome. Activate it width <code>.nice-checkbox</code></p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-1">
                                                <label for="checkbox-1">Checkbox</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-2">
                                                <label for="checkbox-2"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-3">
                                                <label for="checkbox-3"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-4">
                                                <label for="checkbox-4"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-5">
                                                <label for="checkbox-5"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-6">
                                                <label for="checkbox-6"><span class="text-inverse">Checkbox</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-checked-1" checked="checked">
                                                <label for="checkbox-checked-1">Normal</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-checked-2" checked="checked">
                                                <label for="checkbox-checked-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-checked-3" checked="checked">
                                                <label for="checkbox-checked-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-checked-4" checked="checked">
                                                <label for="checkbox-checked-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-checked-5" checked="checked">
                                                <label for="checkbox-checked-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-checked-6" checked="checked">
                                                <label for="checkbox-checked-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-disabled-1" disabled="disabled">
                                                <label for="checkbox-disabled-1">Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-disabled-2" disabled="disabled">
                                                <label for="checkbox-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-disabled-3" disabled="disabled">
                                                <label for="checkbox-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-disabled-4" disabled="disabled">
                                                <label for="checkbox-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-disabled-5" disabled="disabled">
                                                <label for="checkbox-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-disabled-6" disabled="disabled">
                                                <label for="checkbox-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input type="checkbox" id="checkbox-both-1" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-1">Checked - Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input type="checkbox" id="checkbox-both-2" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input type="checkbox" id="checkbox-both-3" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input type="checkbox" id="checkbox-both-4" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input type="checkbox" id="checkbox-both-5" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input type="checkbox" id="checkbox-both-6" checked="checked" disabled="disabled">
                                                <label for="checkbox-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                    <br>

                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Optional style</strong></p>
                                            <p>Just add <code>.checkbox-o</code> to <code>input[type="checkbox"]</code> and you get other Checkbox style.</p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-1">
                                                <label for="checkbox-o-1">Normal</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-2">
                                                <label for="checkbox-o-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-3">
                                                <label for="checkbox-o-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-4">
                                                <label for="checkbox-o-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-5">
                                                <label for="checkbox-o-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-6">
                                                <label for="checkbox-o-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-1" checked="checked">
                                                <label for="checkbox-o-checked-1">Checked</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-2" checked="checked">
                                                <label for="checkbox-o-checked-2"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-3" checked="checked">
                                                <label for="checkbox-o-checked-3"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-4" checked="checked">
                                                <label for="checkbox-o-checked-4"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-5" checked="checked">
                                                <label for="checkbox-o-checked-5"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-checked-6" checked="checked">
                                                <label for="checkbox-o-checked-6"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-1" disabled="disabled">
                                                <label for="checkbox-o-disabled-1">Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-2" disabled="disabled">
                                                <label for="checkbox-o-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-3" disabled="disabled">
                                                <label for="checkbox-o-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-4" disabled="disabled">
                                                <label for="checkbox-o-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-5" disabled="disabled">
                                                <label for="checkbox-o-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-disabled-6" disabled="disabled">
                                                <label for="checkbox-o-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-checkbox">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-1" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-1">Checked - Disabled</label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-primary">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-2" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-success">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-3" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-info">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-4" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-warning">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-5" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->

                                            <div class="nice-checkbox text-danger">
                                                <input class="checkbox-o" type="checkbox" id="checkbox-o-both-6" checked="checked" disabled="disabled">
                                                <label for="checkbox-o-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-checkbox-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                    <br>

                                    <div class="row">
                                        <div class="col-md-offset-2 col-md-10">
                                            <p class="text-muted"><strong>Radio</strong> <code>.nice-radio</code></p>
                                        </div>
                                        <div class="col-md-offset-2 col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radio_1" id="radio-1">
                                                <label for="radio-1">Normal</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radio_2" id="radio-2">
                                                <label for="radio-2"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radio_3" id="radio-3">
                                                <label for="radio-3"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radio_4" id="radio-4">
                                                <label for="radio-4"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radio_5" id="radio-5">
                                                <label for="radio-5"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radio_6" id="radio-6">
                                                <label for="radio-6"><span class="text-inverse">Normal</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radio_1" id="radio-checked-1" checked="checked">
                                                <label for="radio-checked-1">Checked</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radio_2" id="radio-checked-2" checked="checked">
                                                <label for="radio-checked-2"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radio_3" id="radio-checked-3" checked="checked">
                                                <label for="radio-checked-3"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radio_4" id="radio-checked-4" checked="checked">
                                                <label for="radio-checked-4"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radio_5" id="radio-checked-5" checked="checked">
                                                <label for="radio-checked-5"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radio_6" id="radio-checked-6" checked="checked">
                                                <label for="radio-checked-6"><span class="text-inverse">Checked</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radiodis_1" id="radio-disabled-1" disabled="disabled">
                                                <label for="radio-disabled-1">Disabled</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radiodis_2" id="radio-disabled-2" disabled="disabled">
                                                <label for="radio-disabled-2"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radiodis_3" id="radio-disabled-3" disabled="disabled">
                                                <label for="radio-disabled-3"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radiodis_4" id="radio-disabled-4" disabled="disabled">
                                                <label for="radio-disabled-4"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radiodis_5" id="radio-disabled-5" disabled="disabled">
                                                <label for="radio-disabled-5"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radiodis_6" id="radio-disabled-6" disabled="disabled">
                                                <label for="radio-disabled-6"><span class="text-inverse">Disabled</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->

                                        <div class="col-md-2">
                                            <div class="nice-radio">
                                                <input type="radio" name="radiodis_1" id="radio-both-1" checked="checked" disabled="disabled">
                                                <label for="radio-both-1">Checked - Disabled</label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-primary">
                                                <input type="radio" name="radiodis_2" id="radio-both-2" checked="checked" disabled="disabled">
                                                <label for="radio-both-2"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-success">
                                                <input type="radio" name="radiodis_3" id="radio-both-3" checked="checked" disabled="disabled">
                                                <label for="radio-both-3"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-info">
                                                <input type="radio" name="radiodis_4" id="radio-both-4" checked="checked" disabled="disabled">
                                                <label for="radio-both-4"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-warning">
                                                <input type="radio" name="radiodis_5" id="radio-both-5" checked="checked" disabled="disabled">
                                                <label for="radio-both-5"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->

                                            <div class="nice-radio text-danger">
                                                <input type="radio" name="radiodis_6" id="radio-both-6" checked="checked" disabled="disabled">
                                                <label for="radio-both-6"><span class="text-inverse">Checked - Disabled</span></label>
                                            </div><!--/nice-radio-->
                                        </div><!--/col-->
                                    </div><!--/row-->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-rpcdefault -->



                    
                    <div id="panel-inpgroup" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-inpgroup" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-inpgroup" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-inpgroup" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-inpgroup" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Input groups</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="leftaddon">Left Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" id="leftaddon" placeholder="Username">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" placeholder="Username">
                                        </div><!-- /input-group-in -->
                                        <p class="helper-block text-muted"><small>Just add <code>.input-group-in</code> to any input group and you get a beautifull minimalis style.</small></p>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="rightaddon">Right Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="rightaddon">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="bothaddon">Both Addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">$</span>
                                            <input type="text" class="form-control" id="bothaddon">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">$</span>
                                            <input type="text" class="form-control">
                                            <span class="input-group-addon">.00</span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="checkaddon">Checkbox addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <span class="nice-checkbox">
                                                    <input class="checkbox-o" type="checkbox" name="addoncheckbox" id="addoncheckbox1" checked="checked">
                                                    <label for="addoncheckbox1"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="checkaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">
                                                <span class="nice-checkbox">
                                                    <input class="checkbox-o" type="checkbox" name="addoncheckbox" id="addoncheckbox2">
                                                    <label for="addoncheckbox2"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="checkaddon">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="radioaddon">Radio addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">
                                                <span class="nice-radio text-primary">
                                                    <input type="radio" name="addonradio" id="addonradio1" checked="checked">
                                                    <label for="addonradio1"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="radioaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon">
                                                <span class="nice-radio text-primary">
                                                    <input type="radio" name="addonradio" id="addonradio2">
                                                    <label for="addonradio2"></label>
                                                </span>
                                            </span>
                                            <input type="text" class="form-control" id="radioaddon">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddon">Button addon</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-btn">
                                                <button class="btn btn-inverse" type="button">Go!</button>
                                            </span>
                                            <input type="text" class="form-control" id="btnaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-btn">
                                                <button class="btn btn-inverse" type="button"><i class="fa fa-rocket"></i></button>
                                            </span>
                                            <input type="text" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddonright">Right button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="btnaddonright">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button">Go!</button>
                                            </span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-search"></i></button>
                                            </span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="btnaddonboth">Both button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-paperclip"></i></button>
                                            </span>
                                            <input type="text" class="form-control" id="btnaddonboth">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-share"></i></button>
                                            </span>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-paperclip"></i></button>
                                            </span>
                                            <input type="text" class="form-control">
                                            <span class="input-group-btn">
                                                <button class="btn btn-primary" type="button"><i class="fa fa-share"></i></button>
                                            </span>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="dropaddon">Dropdown button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">Action <i class="fa fa-angle-down"></i></button>
                                                <ul class="dropdown-menu">
                                                    <li><a href="form-basic.php#">Action</a></li>
                                                    <li><a href="form-basic.php#">Another action</a></li>
                                                    <li><a href="form-basic.php#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="form-basic.php#">Separated link</a></li>
                                                </ul>
                                            </div><!-- /btn-group -->
                                            <input type="text" class="form-control" id="dropaddon">
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-inverse dropdown-toggle" data-toggle="dropdown">Action <i class="fa fa-angle-down"></i></button>
                                                <ul class="dropdown-menu">
                                                    <li><a href="form-basic.php#">Action</a></li>
                                                    <li><a href="form-basic.php#">Another action</a></li>
                                                    <li><a href="form-basic.php#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="form-basic.php#">Separated link</a></li>
                                                </ul>
                                            </div><!-- /btn-group -->
                                            <input type="text" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="segmentaddon">Segmented button</label>
                                    <div class="col-sm-5">
                                        <div class="input-group">
                                            <input type="text" class="form-control" id="segmentaddon">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-primary" tabindex="-1">Action</button>
                                                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" tabindex="-1">
                                                    <i class="fa fa-info"></i>
                                                </button>
                                                <ul class="dropdown-menu" role="menu">
                                                    <li><a href="form-basic.php#">Action</a></li>
                                                    <li><a href="form-basic.php#">Another action</a></li>
                                                    <li><a href="form-basic.php#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="form-basic.php#">Separated link</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /input-group -->
                                        <br>
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control">
                                            <div class="input-group-btn">
                                                <button type="button" class="btn btn-primary" tabindex="-1"><i class="fa fa-paperclip"></i></button>
                                                <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" tabindex="-1">
                                                    <i class="fa fa-share"></i>
                                                </button>
                                                <ul class="dropdown-menu" role="menu">
                                                    <li><a href="form-basic.php#">Action</a></li>
                                                    <li><a href="form-basic.php#">Another action</a></li>
                                                    <li><a href="form-basic.php#">Something else here</a></li>
                                                    <li class="divider"></li>
                                                    <li><a href="form-basic.php#">Separated link</a></li>
                                                </ul>
                                            </div>
                                        </div><!-- /input-group-in -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-inpgroup -->




                    <div id="panel-ctrlstate" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-ctrlstate" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-ctrlstate" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-ctrlstate" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-ctrlstate" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Control states</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="disabledInput">Disabled input</label>
                                    <div class="col-md-5">
                                        <input class="form-control" id="disabledInput" type="text" placeholder="Disabled input here..." disabled="disabled">
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="disabledSelect">Disabled select menu</label>
                                    <div class="col-md-5">
                                        <select id="disabledSelect" class="form-control text-muted" disabled="disabled">
                                            <option>Disabled select</option>
                                        </select>
                                        <div class="checkbox">
                                            <label>
                                                <input type="checkbox" disabled="disabled"> <span class="text-muted">Can't check this</span>
                                            </label>
                                        </div>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success">
                                    <label class="col-sm-3 control-label" for="inputSuccess">Input with success</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputSuccess">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning">
                                    <label class="col-sm-3 control-label" for="inputWarning">Input with warning</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputWarning">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error">
                                    <label class="col-sm-3 control-label" for="inputError">Input with error</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="inputError">
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success">
                                    <label class="col-sm-3 control-label" for="addonSucces">Success with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonSucces">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning">
                                    <label class="col-sm-3 control-label" for="addonWarning">Warning with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonWarning">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error">
                                    <label class="col-sm-3 control-label" for="addonError">Error with addon</label>
                                    <div class="col-md-5">
                                        <div class="input-group">
                                            <span class="input-group-addon">@</span>
                                            <input type="text" class="form-control" name="addonError">
                                        </div><!-- /input-group -->
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-success has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsSuccess">Success with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsSuccess">
                                        <span class="glyphicon glyphicon-ok form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-warning has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsWarning">Warning with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsWarning">
                                        <span class="glyphicon glyphicon-warning-sign form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->

                                <div class="form-group has-error has-feedback">
                                    <label class="col-sm-3 control-label" for="iconsError">Error with icons</label>
                                    <div class="col-md-5">
                                        <input type="text" class="form-control" id="iconsError">
                                        <span class="glyphicon glyphicon-remove form-control-feedback"></span>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-ctrlstate -->




                    <div id="panel-ctrlsize" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-ctrlsize" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-ctrlsize" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-ctrlsize" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-ctrlsize" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Control sizing</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="inputSizing">Input Sizing</label>
                                    <div class="col-md-5">
                                        <input id="inputSizing" class="form-control input-lg" type="text" placeholder=".input-lg"> <br>
                                        <input class="form-control" type="text" placeholder="Default input"> <br>
                                        <input class="form-control input-sm" type="text" placeholder=".input-sm"> <br>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="selectSizing">Select Sizing</label>
                                    <div class="col-md-5">
                                        <select id="selectSizing" class="form-control input-lg">
                                            <option>.input-lg</option>
                                        </select> <br>
                                        <select class="form-control">
                                            <option>Default input</option>
                                        </select> <br>
                                        <select class="form-control input-sm">
                                            <option>.input-sm</option>
                                        </select>
                                    </div>
                                </div><!-- /form-group -->

                                <div class="form-group">
                                    <p class="text-muted"><strong>Column sizing</strong></p>
                                    <div class="row">
                                        <div class="col-md-12">
                                            <input type="text" class="form-control" placeholder=".col-md-12">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <input type="text" class="form-control" placeholder=".col-md-6">
                                        </div>
                                        <div class="col-md-6">
                                            <input type="text" class="form-control" placeholder=".col-md-6">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                        <div class="col-md-4">
                                            <input type="text" class="form-control" placeholder=".col-md-4">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                        <div class="col-md-3">
                                            <input type="text" class="form-control" placeholder=".col-md-3">
                                        </div>
                                    </div><!-- /row -->
                                    <br>
                                    <div class="row">
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                        <div class="col-md-2">
                                            <input type="text" class="form-control" placeholder=".col-md-2">
                                        </div>
                                    </div><!-- /cols -->
                                </div><!-- /form-group -->
                            </form><!-- /form -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-ctrlsize -->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="form-basic.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="form-basic.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="form-basic.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="form-basic.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="form-basic.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="form-basic.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="form-basic.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="form-basic.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="form-basic.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="form-basic.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="form-basic.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="form-basic.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="form-basic.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="form-basic.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="form-basic.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="form-basic.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="form-basic.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="form-basic.php#top"><i class="fa fa-arrow-up"></i></a>
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
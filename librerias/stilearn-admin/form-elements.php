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
                    <a href="form-elements.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="form-elements.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="form-elements.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="form-elements.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="form-elements.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="form-elements.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-elements.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="form-elements.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-elements.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="form-elements.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="form-elements.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="form-elements.php#">
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
                            <a class="view-all" tabindex="-1" href="form-elements.php#">
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
                        <a href="form-elements.php#">
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
                        <a href="form-elements.php#">
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
                        <a href="form-elements.php#">
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
                        <a href="form-elements.php#">
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
                        <a href="form-elements.php#" data-pjax=".content-body">
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
                        <a href="form-elements.php#" data-pjax=".content-body">
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
                        <a href="form-elements.php#">
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
                        <a class="item-ch-extra" href="form-elements.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="form-elements.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="form-elements.php#">
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
                            <a href="form-elements.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="form-elements.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="form-elements.php#">Some Action</a></li>
                                <li><a href="form-elements.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="form-elements.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="form-elements.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="form-elements.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- FORM ELEMENTS
                    ================================================== -->
                    <!-- TYPEAHEAD.JS -->
                    <div id="panel-typeahead" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-typeahead" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-typeahead" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-typeahead" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-typeahead" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Typeahead AutoComplete</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="typeahead-local">Single Dataset <em>(Local)</em></label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="glyphicon glyphicon-user"></i></span>
                                            <input type="text" id="typeahead-local" class="form-control" placeholder="Look a team">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="typeahead-prefetches">Prefetches data</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" id="typeahead-prefetches" class="form-control" placeholder="Countries">
                                            <span class="input-group-addon text-silver"><i class="fa fa-flag-o"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="typeahead-customtemplate">Custom template</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" id="typeahead-customtemplate" class="form-control" placeholder="Open source projects by Twitter">
                                            <span class="input-group-btn">
                                                <a rel="tooltip" title="See all projects" target="_blank" href="http://twitter.github.io/" class="btn">
                                                    <i class="fa fa-twitter text-silver"></i>
                                                </a>
                                            </span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="typeahead-2datasets">Two datasets</label>
                                    <div class="col-sm-5">
                                        <input type="text" id="typeahead-2datasets" class="form-control" placeholder="NBA and NHL teams">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-typeahead -->



                    <!-- MASK INPUT -->
                    <div id="panel-mask" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-mask" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-mask" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-mask" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-mask" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Input Mask</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Make masks on form fields and html elements, use with simple data attribute <code>data-mask="mask-type"</code>. Available data mask <em>(To customize please read <a target="_blank" href="http://igorescobar.github.io/jQuery-Mask-Plugin/">Mask Plugin Docs</a>)</em>:</p>
                            <p><pre class="prettyprint">'date', 'time', 'date_time', 'zip', 'money', 'phone', 'phone_with_ddd', 'phone_us', 'cpf', 'ip_address', 'percent'</pre></p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-date">Date</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-calendar"></i></span>
                                            <input type="text" data-mask="date" id="mask-date" class="form-control" placeholder="dd/mm/yyyy">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-time">Time</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-clock-o"></i></span>
                                            <input type="text" data-mask="time" id="mask-time" class="form-control" placeholder="hh:mm:ss">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-datetime">Date and Time</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-calendar-o"></i></span>
                                            <input type="text" data-mask="date_time" id="mask-datetime" class="form-control" placeholder="dd/mm/yyyy hh:mm:ss">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-zip">Zip-Code</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-road"></i></span>
                                            <input type="text" data-mask="zip" id="mask-zip" class="form-control" placeholder="00000-000">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-money">Money</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-money"></i></span>
                                            <input type="text" data-mask="money" id="mask-money" class="form-control" placeholder="0,000.00">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-phone">Telephone</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-phone"></i></span>
                                            <input type="text" data-mask="phone" id="mask-phone" class="form-control" placeholder="0000-0000">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-phonecode">Telephone with Code</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-mobile-phone"></i></span>
                                            <input type="text" data-mask="phone_with_ddd" id="mask-phonecode" class="form-control" placeholder="(00) 0000-0000">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-usphone">US Telephone</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-phone"></i></span>
                                            <input type="text" data-mask="phone_us" id="mask-usphone" class="form-control" placeholder="(000) 000-0000">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-cpf">CPF</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-location-arrow"></i></span>
                                            <input type="text" data-mask="cpf" id="mask-cpf" class="form-control" placeholder="000.000.000-00">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-ip">IP Address</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-cloud"></i></span>
                                            <input type="text" data-mask="ip_address" id="mask-ip" class="form-control" placeholder="000.000.000.000">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="mask-percent">Percent</label>
                                    <div class="col-sm-5">
                                        <input type="text" data-mask="percent" id="mask-percent" class="form-control" placeholder="0,00%">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-mask -->




                    <!-- TAGS INPUT -->
                    <div id="panel-tagsinput" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-tagsinput" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-tagsinput" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-tagsinput" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-tagsinput" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Tags Input</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="tagsinput">Tags Input</label>
                                    <div class="col-sm-5">
                                        <input type="text" id="tagsinput" data-input="tags" class="form-control" value="php,ios,javascript,ruby,android,kindle" placeholder="Add input">
                                        <p class="helper-block">Use with <code>.tags-input</code> or <code>data-input="tags"</code>, Very easy!</p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-tagsinput -->




                    <!-- MULTISELECT -->
                    <div id="panel-multiselect" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-multiselect" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-multiselect" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-multiselect" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-multiselect" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Multiselect</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <div class="col-sm-offset-4 col-sm-8">
                                        <select data-input="multiselect" multiple="multiple">
                                            <option value="Courtney_Wilkins" selected="selected">Courtney Wilkins</option>
                                            <option value="Rama_Obrien" selected="selected">Rama Obrien</option>
                                            <option value="Ross_Mills">Ross Mills</option>
                                            <option value="Craig_Banks">Craig Banks</option>
                                            <option value="Rae_Franco">Rae Franco</option>
                                            <option value="Darrel_Carlson" selected="selected">Darrel Carlson</option>
                                            <option value="Lynn_Mcbride">Lynn Mcbride</option>
                                            <option value="Noelle_Martinez">Noelle Martinez</option>
                                            <option value="Risa_Fletcher">Risa Fletcher</option>
                                            <option value="Dennis_Mejia" disabled="disabled">Dennis Mejia</option>
                                            <option value="Blaze_Eaton">Blaze Eaton</option>
                                            <option value="Theodore_Kelly">Theodore Kelly</option>
                                            <option value="Roth_Velazquez" selected="selected">Roth Velazquez</option>
                                            <option value="Xena_Holden">Xena Holden</option>
                                            <option value="Deirdre_Rodriquez" disabled="disabled">Deirdre Rodriquez</option>
                                            <option value="Nita_Marquez">Nita Marquez</option>
                                            <option value="Amanda_Hicks" selected="selected">Amanda Hicks</option>
                                            <option value="Alan_Ford">Alan Ford</option>
                                            <option value="Judith_Talley">Judith Talley</option>
                                            <option value="Kuame_Boyle">Kuame Boyle</option>
                                        </select>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-multiselect -->




                    <!-- SELECT2 & SELECTBOXIT -->
                    <div id="panel-inpselect" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-inpselect" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-inpselect" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-inpselect" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-inpselect" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Replaced Select</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <h4>Select2 plugin</h4>
                            <p>Easy to use with data attribute <code>data-input="select2"</code> for Select mode and <code>data-input="select2-tags"</code> for Input Tags mode. Or you can use <code>.select2</code> and <code>.select2-tags</code>. If you use Select2 Tags you can define your available tags with <code>data-tags="your,tags,value"</code> (use <code>,</code> to separate your value), like demo below.</p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label" for="select2">Select2</label>
                                    <div class="col-sm-5">
                                        <select style="width:100%" data-input="select2" placeholder="Select your time zone">
                                            <option value=""></option>
                                            <optgroup label="Alaskan/Hawaiian Time Zone">
                                                <option value="AK">Alaska</option>
                                                <option value="HI">Hawaii</option>
                                            </optgroup>
                                            <optgroup label="Pacific Time Zone">
                                                <option value="CA">California</option>
                                                <option value="NV">Nevada</option>
                                                <option value="OR">Oregon</option>
                                                <option value="WA">Washington</option>
                                            </optgroup>
                                            <optgroup label="Mountain Time Zone">
                                                <option value="AZ">Arizona</option>
                                                <option value="CO">Colorado</option>
                                                <option value="ID">Idaho</option>
                                                <option value="MT">Montana</option>
                                                <option value="NE">Nebraska</option>
                                                <option value="NM">New Mexico</option>
                                                <option value="ND">North Dakota</option>
                                                <option value="UT">Utah</option>
                                                <option value="WY">Wyoming</option>
                                            </optgroup>
                                            <optgroup label="Central Time Zone">
                                                <option value="AL">Alabama</option>
                                                <option value="AR">Arkansas</option>
                                                <option value="IL">Illinois</option>
                                                <option value="IA">Iowa</option>
                                                <option value="KS">Kansas</option>
                                                <option value="KY">Kentucky</option>
                                                <option value="LA">Louisiana</option>
                                                <option value="MN">Minnesota</option>
                                                <option value="MS">Mississippi</option>
                                                <option value="MO">Missouri</option>
                                                <option value="OK">Oklahoma</option>
                                                <option value="SD">South Dakota</option>
                                                <option value="TX">Texas</option>
                                                <option value="TN">Tennessee</option>
                                                <option value="WI">Wisconsin</option>
                                            </optgroup>
                                            <optgroup label="Eastern Time Zone">
                                                <option value="CT">Connecticut</option>
                                                <option value="DE">Delaware</option>
                                                <option value="FL">Florida</option>
                                                <option value="GA">Georgia</option>
                                                <option value="IN">Indiana</option>
                                                <option value="ME">Maine</option>
                                                <option value="MD">Maryland</option>
                                                <option value="MA">Massachusetts</option>
                                                <option value="MI">Michigan</option>
                                                <option value="NH">New Hampshire</option>
                                                <option value="NJ">New Jersey</option>
                                                <option value="NY">New York</option>
                                                <option value="NC">North Carolina</option>
                                                <option value="OH">Ohio</option>
                                                <option value="PA">Pennsylvania</option>
                                                <option value="RI">Rhode Island</option>
                                                <option value="SC">South Carolina</option>
                                                <option value="VT">Vermont</option>
                                                <option value="VA">Virginia</option>
                                                <option value="WV">West Virginia</option>
                                            </optgroup>
                                        </select>
                                        <br><br>
                                        <select style="width:100%" data-input="select2" placeholder="Multiple select" multiple="multiple">
                                            <optgroup label="Alaskan/Hawaiian Time Zone">
                                                <option value="AK">Alaska</option>
                                                <option value="HI">Hawaii</option>
                                            </optgroup>
                                            <optgroup label="Pacific Time Zone">
                                                <option value="CA">California</option>
                                                <option value="NV">Nevada</option>
                                                <option value="OR">Oregon</option>
                                                <option value="WA">Washington</option>
                                            </optgroup>
                                            <optgroup label="Mountain Time Zone">
                                                <option value="AZ">Arizona</option>
                                                <option value="CO">Colorado</option>
                                                <option value="ID">Idaho</option>
                                                <option value="MT">Montana</option>
                                                <option value="NE">Nebraska</option>
                                                <option value="NM">New Mexico</option>
                                                <option value="ND">North Dakota</option>
                                                <option value="UT">Utah</option>
                                                <option value="WY">Wyoming</option>
                                            </optgroup>
                                            <optgroup label="Central Time Zone">
                                                <option value="AL">Alabama</option>
                                                <option value="AR">Arkansas</option>
                                                <option value="IL">Illinois</option>
                                                <option value="IA">Iowa</option>
                                                <option value="KS">Kansas</option>
                                                <option value="KY">Kentucky</option>
                                                <option value="LA">Louisiana</option>
                                                <option value="MN">Minnesota</option>
                                                <option value="MS">Mississippi</option>
                                                <option value="MO">Missouri</option>
                                                <option value="OK">Oklahoma</option>
                                                <option value="SD">South Dakota</option>
                                                <option value="TX">Texas</option>
                                                <option value="TN">Tennessee</option>
                                                <option value="WI">Wisconsin</option>
                                            </optgroup>
                                            <optgroup label="Eastern Time Zone">
                                                <option value="CT">Connecticut</option>
                                                <option value="DE">Delaware</option>
                                                <option value="FL">Florida</option>
                                                <option value="GA">Georgia</option>
                                                <option value="IN">Indiana</option>
                                                <option value="ME">Maine</option>
                                                <option value="MD">Maryland</option>
                                                <option value="MA">Massachusetts</option>
                                                <option value="MI">Michigan</option>
                                                <option value="NH">New Hampshire</option>
                                                <option value="NJ">New Jersey</option>
                                                <option value="NY">New York</option>
                                                <option value="NC">North Carolina</option>
                                                <option value="OH">Ohio</option>
                                                <option value="PA">Pennsylvania</option>
                                                <option value="RI">Rhode Island</option>
                                                <option value="SC">South Carolina</option>
                                                <option value="VT">Vermont</option>
                                                <option value="VA">Virginia</option>
                                                <option value="WV">West Virginia</option>
                                            </optgroup>
                                        </select>
                                        <br><br>
                                        <input style="width:100%" type="hidden" data-input="select2-tags" value="php,html3,css3" data-tags="php,ios,javascript,ruby,android,kindle,html5,css3,java">
                                        <br><br>
                                        <select style="width:100%" data-input="select2" placeholder="Disable state" disabled="disabled">
                                            <option value=""></option>
                                        </select>
                                        <br><br>
                                        <select style="width:100%" data-input="select2" placeholder="Disable state" multiple="multiple" disabled="disabled"></select>
                                    </div><!--/cols-->
                                </div><!--/form-group-->
                            </form><!--/form-->

                            <h4>SelectBoxIt</h4>
                            <p>Just provides an alternative option to you to use form <code>select</code> with SelectBoxIt. Use with <code>data-input="selectboxit"</code> or <code>.selectboxit</code>.</p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label">SelectBoxIt</label>
                                    <div class="col-sm-5">
                                        <select data-input="selectboxit" placeholder="Select city">
                                            <option value="AK">Alaska</option>
                                            <option value="HI">Hawaii</option>
                                            <option value="CA">California</option>
                                            <option value="NV">Nevada</option>
                                            <option value="OR">Oregon</option>
                                            <option value="WA">Washington</option>
                                        </select>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Cutom arrow</label>
                                    <div class="col-sm-5">
                                        <select data-input="selectboxit" placeholder="Select city" data-arrow="fa fa-location-arrow">
                                            <option value="AK">Alaska</option>
                                            <option value="HI">Hawaii</option>
                                            <option value="CA">California</option>
                                            <option value="NV">Nevada</option>
                                            <option value="OR">Oregon</option>
                                            <option value="WA">Washington</option>
                                        </select>
                                        <p class="help-block"><code>data-arrow</code> support with <em>Glyphicon </em> and <em>Font Awesome Icons</em></p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Native mode</label>
                                    <div class="col-sm-5">
                                        <select data-input="selectboxit" placeholder="Select city" data-native="">
                                            <option value="AK">Alaska</option>
                                            <option value="HI">Hawaii</option>
                                            <option value="CA">California</option>
                                            <option value="NV">Nevada</option>
                                            <option value="OR">Oregon</option>
                                            <option value="WA">Washington</option>
                                        </select>
                                        <p class="help-block"><code>data-native</code> give you a native style</p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Icon & Image</label>
                                    <div class="col-sm-5">
                                        <select data-input="selectboxit" multiple="multiple">
                                            <option value="Select a struff:" data-iconurl="http://icons.iconarchive.com/icons/custom-icon-design/pretty-office-5/256/themes-icon.png">
                                                Select a struff
                                            </option>
                                            <option value="Twitter Bootstrap" data-iconurl="http://blog.getbootstrap.com/public/ico/apple-touch-icon-144-precomposed.png">
                                                Twitter Bootstrap
                                            </option>
                                            <option value="jQuery UI" data-iconurl="http://c747925.r25.cf2.rackcdn.com/blog/wp-content/uploads/2010/09/jquery-ui-logo.png">
                                                jQuery UI
                                            </option>
                                            <option value="jQuery Mobile" data-icon="glyphicon glyphicon-phone">
                                                jQuery Mobile
                                            </option>
                                            <option value="HTML5" data-icon="fa fa-html5">
                                                HTML5
                                            </option>
                                            <option value="CSS3" data-icon="fa fa-css3">
                                                CSS3
                                            </option>
                                        </select>
                                        <p class="help-block">Support with <em>Glyphicon </em> and <em>Font Awesome Icons</em></p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->
                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-inpselect -->




                    <!-- DATE RANGE PICKER -->
                    <div id="panel-daterangepicker" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-daterangepicker" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-daterangepicker" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-daterangepicker" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-daterangepicker" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Date Range Picker</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Usa with attribute <code>data-input="daterangepicker"</code>, and support with <code>data-time</code> to enable time picker and <code>data-format</code> to format output date. More usage please <a target="_blank" href="http://www.dangrossman.info/2012/08/20/a-date-range-picker-for-twitter-bootstrap/">read the Docs</a>.</p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Basic Date Range Picker</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-calendar"></i></span>
                                            <input type="text" data-input="daterangepicker" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Date & Time Picker</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="daterangepicker" data-time="true" data-format="MM/DD/YYYY h:mm A" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-clock-o"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Pre-defined Ranges & Callback</label>
                                    <div class="col-sm-5">
                                        <button id="reportrange" class="btn btn-icon btn-inverse pull-right">
                                            <i class="fa fa-calendar"></i> <span>Please select Date Range</span>
                                        </button>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-daterangepicker -->




                    <!-- DATE PICKER -->
                    <div id="panel-datepicker" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-datepicker" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-datepicker" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-datepicker" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-datepicker" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Date Picker</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Basic usage with <code>data-input="datepicker"</code></p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Inline Datepicker</label>
                                    <div class="col-sm-5">
                                        <div data-input="datepicker"></div>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">As Input</label>
                                    <div class="col-sm-5">
                                        <input type="text" data-input="datepicker" class="form-control">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">As Component</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in date" data-input="datepicker" data-format="yyyy/mm/dd">
                                            <input type="text" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-calendar"></i></span>
                                        </div><!-- /input-group-in -->
                                        <p class="helper-block">Required <code>.date</code></p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Start view mode</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-calendar"></i></span>
                                            <input type="text" data-input="datepicker" data-view="2" class="form-control">
                                        </div><!-- /input-group-in -->
                                        <p class="helper-block">Use with <code>data-view="value"</code> (posible value <code>(int) 0, 1 or 2</code>)</p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-datepicker -->




                    <!-- TIME PICKER -->
                    <div id="panel-timepicker" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-timepicker" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-timepicker" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-timepicker" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-timepicker" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Time Picker</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Basic usage with <code>data-input="timepicker"</code></p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Basic Time Picker</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <span class="input-group-addon text-silver"><i class="fa fa-clock-o"></i></span>
                                            <input type="text" data-input="timepicker" class="form-control">
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Dropdown</label>
                                    <div class="col-sm-5">
                                        <input type="text" data-input="timepicker" data-template="dropdown" class="form-control">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">As Component <small>(24hr)</small></label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" class="form-control" data-input="timepicker" data-template="dropdown" data-show-meridian="false">
                                            <span class="input-group-addon text-silver"><i class="fa fa-clock-o"></i></span>
                                        </div><!-- /input-group-in -->
                                        <p class="helper-block text-muted"><small>Disable Meridian</small></p>
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">With Datepicker</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="datepicker" data-view="2" class="form-control">
                                            <input type="hidden" id="fake-timepicker" class="form-control">
                                            <span class="input-group-addon text-silver" data-input="timepicker" data-fake-input="#fake-timepicker" data-template="dropdown"><i class="fa fa-clock-o"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-timepicker -->




                    <!-- COLOR PICKER -->
                    <div id="panel-colorpicker" class="panel panel-default sortable-widget-item">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-colorpicker" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-colorpicker" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-colorpicker" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-colorpicker" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Color Picker</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p>Basic usage with <code>data-input="colorpicker"</code></p>
                            <form role="form" class="form-horizontal form-bordered">
                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Default <small>(Hue)</small></label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="colorpicker" value="#13A89E" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-tint"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Saturation <small>(Letter Case)</small></label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="colorpicker" value="#5BB75B" data-control="saturation" data-lettercase="uppercase" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-tint"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Brightness</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="colorpicker" value="#FAA732" data-control="brightness" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-tint"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Wheel</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="colorpicker" data-control="wheel" value="#DA4F49" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-tint"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Opacity</label>
                                    <div class="col-sm-5">
                                        <div class="input-group input-group-in">
                                            <input type="text" data-input="colorpicker" data-opacity=".5" value="#49AFCD" class="form-control">
                                            <span class="input-group-addon text-silver"><i class="fa fa-tint"></i></span>
                                        </div><!-- /input-group-in -->
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Inline</label>
                                    <div class="col-sm-5">
                                        <input type="text" data-input="colorpicker" data-inline="true" value="#394264" class="form-control">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                                <div class="form-group">
                                    <label class="col-sm-3 control-label">Hidden Input</label>
                                    <div class="col-sm-5">
                                        <input type="hidden" data-input="colorpicker" value="#394264" data-position="top right" class="form-control">
                                    </div><!--/cols-->
                                </div><!--/form-group-->

                            </form><!--/form-->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-colorpicker -->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="form-elements.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="form-elements.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="form-elements.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="form-elements.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="form-elements.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="form-elements.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="form-elements.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="form-elements.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="form-elements.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="form-elements.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="form-elements.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="form-elements.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="form-elements.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="form-elements.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="form-elements.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="form-elements.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="form-elements.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="form-elements.php#top"><i class="fa fa-arrow-up"></i></a>
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
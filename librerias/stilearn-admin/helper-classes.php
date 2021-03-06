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
                    <a href="helper-classes.php#" class="dropdown-toggle" data-toggle="dropdown">
                        <span class="fa fa-angle-down"></span>
                    </a>
                    <ul class="dropdown-menu animated flipInX pull-right" role="menu">
                        <li><a href="helper-classes.php#"><i class="fa fa-user"></i> Profile</a></li>
                        <li><a href="helper-classes.php#"><i class="fa fa-envelope"></i> Inbox</a></li>
                        <li><a href="helper-classes.php#"><i class="fa fa-tasks"></i> Tasks</a></li>
                        <li class="divider"></li>
                        <li><a href="helper-classes.php#"><i class="fa fa-sign-out"></i> Log Out</a></li>
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
                    <a href="helper-classes.php#" title="View site">
                        <i class="header-menu-icon icon-only fa fa-rocket"></i>
                    </a>
                </li><!-- /header-menu-item -->
                <li>
                    <a href="helper-classes.php#" title="Notifications" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-success">4</span>
                        <i class="header-menu-icon icon-only fa fa-warning"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Notofications</li><!-- /dropdown-header -->
                        <li class="notif-minimal" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-primary">
                                    <i class="fa fa-heart-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evelyn</span> favorite your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-warning">
                                    <i class="fa fa-user"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Evans</span> register as a Member</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-shopping-cart"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Katherine</span> purchase an Item</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-danger">
                                    <i class="fa fa-comment-o"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Gomez</span> Comment on your Post</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-info">
                                    <i class="fa fa-twitter"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Willie</span> is now following you</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-ico bg-success">
                                    <i class="fa fa-cloud-upload"></i>
                                </div>
                                <p class="notif-text"><span class="text-bold">Nguyen</span> upload new Portofolio</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="helper-classes.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all notifications
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="helper-classes.php#" title="Inboxs" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-warning animated animated-repeat flash">3</span>
                        <i class="header-menu-icon icon-only fa fa-envelope-o"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">You have 3 new messages</li><!-- /dropdown-header -->
                        <li class="notif-media" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/8af46bf8.uifaces21.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Account Team <small>58 min</small></h3>
                                <p class="notif-text">Spread the Word & Earn!</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b0f7e705.uifaces5.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Timothy Lucas, Me (2) <small>Wed</small></h3>
                                <p class="notif-text">Elit odio, sed leo ligula semper, vehicula maecenas, eros fusce</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/b7f97507.uifaces4.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Raymond Rios <small>Tue</small></h3>
                                <p class="notif-text">Risus suscipit urna, tristique molestie vestibulum nunc tempor ultricies</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/690243f1.uifaces6.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Stilearning <small>Tue</small></h3>
                                <p class="notif-text">Thanks for ordering Stilearn Admin (order #WD12345678)</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/a0c1c960.uifaces9.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">andrea.olson@mail.com <small>Mon</small></h3>
                                <p class="notif-text">Lectus curabitur mauris arcu donec morbi diam</p>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-img pull-left">
                                    <img src="images/dummy/e7dd5f45.uifaces8.jpg" alt="" class="img-circle">
                                </div>
                                <h3 class="notif-heading">Nicole Miller <small>Mon</small></h3>
                                <p class="notif-text">Approval for new design!</p>
                            </a><!-- /notif-item -->
                        </li><!-- /dropdown-alert -->
                        <li class="dropdown-footer bg-cloud">
                            <a class="view-all" tabindex="-1" href="helper-classes.php#">
                                <i class="fa fa-angle-right pull-right"></i> See all messages
                            </a>
                        </li><!-- /dropdown-footer -->
                    </ul><!-- /dropdown-extend -->
                </li><!-- /header-menu-item -->
                <li>
                    <a href="helper-classes.php#" title="Tasks" class="dropdown-toggle" data-toggle="dropdown" role="button">
                        <span class="badge badge-danger">7</span>
                        <i class="header-menu-icon icon-only fa fa-tasks"></i>
                    </a>
                    <ul class="dropdown-menu dropdown-extend animated fadeInDown pull-right" role="menu">
                        <li class="dropdown-header">Tasks progress</li><!-- /dropdown-header -->
                        <li class="notif-progress" data-toggle="niceScroll" data-scroll-cursorcolor="#ecf0f1">
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">60%</div>
                                <div class="notif-text">Uploading...</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                                        <span class="sr-only">60% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">33%</div>
                                <div class="notif-text">Upgrade Theme</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="33" aria-valuemin="0" aria-valuemax="100" style="width: 33%">
                                        <span class="sr-only">33% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">87%</div>
                                <div class="notif-text">Webapp Development</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" style="width: 87%">
                                        <span class="sr-only">87% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">54%</div>
                                <div class="notif-text">Backup Data</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="54" aria-valuemin="0" aria-valuemax="100" style="width: 54%">
                                        <span class="sr-only">54% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">92%</div>
                                <div class="notif-text">Bandwidth Limit</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" style="width: 92%">
                                        <span class="sr-only">92% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">26%</div>
                                <div class="notif-text">Clean System</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="26" aria-valuemin="0" aria-valuemax="100" style="width: 26%">
                                        <span class="sr-only">26% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
                                <div class="notif-text pull-right">100%</div>
                                <div class="notif-text">Done with warning</div>
                                <div class="progress progress-sm">
                                    <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                                        <span class="sr-only">100% Complete</span>
                                    </div>
                                </div>
                            </a><!-- /notif-item -->
                            <a class="notif-item" href="helper-classes.php#">
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
                            <a class="view-all" tabindex="-1" href="helper-classes.php#">
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
                        <a href="helper-classes.php#">
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
                        <a href="helper-classes.php#">
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
                        <a href="helper-classes.php#">
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
                        <a href="helper-classes.php#">
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
                        <a href="helper-classes.php#" data-pjax=".content-body">
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
                        <a href="helper-classes.php#" data-pjax=".content-body">
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
                        <a href="helper-classes.php#">
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
                        <a class="item-ch-extra" href="helper-classes.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-barcolor="#5BB75B" data-value="0,5,3,9,6,5,9,7,3,5,2"></span>
                            <div class="data-text text-success">
                                765K <p class="text-muted">Visits</p>
                            </div>
                        </a><!--/item-ch-extra-->
                        
                        <div class="divider"></div>
                        
                        <a class="item-ch-extra" href="helper-classes.php#">
                            <span class="sparkline-bar" data-height="36px" data-barwidth="3" data-value="0,9,7,9,6,3,5,3,5,5,2"></span>
                            <div class="data-text text-primary">
                                1437 <p class="text-muted">Users</p>
                            </div>
                        </a><!--/item-ch-extra-->

                        <div class="divider"></div>

                        <a class="item-ch-extra" href="helper-classes.php#">
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
                            <a href="helper-classes.php#">
                                <i class="fa fa-money"></i> Orders <span class="text-danger">(+12)</span>
                            </a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="helper-classes.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-user"></i> Users <span class="text-danger">(+34)</span>
                                <i class="fa fa-angle-down"></i>
                            </a>                            
                            <ul class="dropdown-menu animated flipInX pull-right">
                                <li><a href="helper-classes.php#">Some Action</a></li>
                                <li><a href="helper-classes.php#">Other Action</a></li>
                                <li class="divider"></li>
                                <li><a href="helper-classes.php#">Something Else</a></li>
                            </ul>
                        </li>
                        <li class="divider"></li>
                        <li rel="popover-left" data-context="inverse" data-trigger="hover" data-content="Click me to toggle Chat box!">
                            <a data-toggle="side-right" href="helper-classes.php#">
                                Hangouts <i class="fa fa-comment-o animated animated-repeat flash"></i>
                            </a>
                        </li>
                    </ul><!--/control-nav-->
                    
                    <!--breadcrumb-->
                    <ul class="breadcrumb">
                        <li><a href="index.php"><i class="fa fa-home"></i> Dashboard</a></li>
                        <li><a href="helper-classes.php#">Library</a></li>
                        <li class="active">Data</li>
                    </ul><!--/breadcrumb-->
                </div><!-- /content-control -->

                <div class="content-body">
                    <!-- APP CONTENT
                    ================================================== -->
                                        <!-- HELPER CLASS
                    ================================================== -->
                    <!-- HELPER CLASS & RESPONSIVE UTILITIES  -->
                    <div id="panel-helpclass" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-helpclass" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-helpclass" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-helpclass" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-helpclass" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Helper Classes</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <div class="row">
                                <div class="col-md-6">
                                    <p class="text-muted"><strong>Close icon</strong></p>
                                    <p>Use the generic close icon for dismissing content like modals and alerts.</p>
                                    <p><button type="button" class="close" aria-hidden="true" style="float:none">&times;</button></p>
                                    <pre class="prettyprint">&lt;button type=&quot;button&quot; class=&quot;close&quot; aria-hidden=&quot;true&quot;&gt;&amp;times;&lt;/button&gt;</pre>
                                    <br>
                                    
                                    <p class="text-muted" id="helper-classes-floats"><strong>Quick floats</strong></p>
                                    <p>Float an element to the left or right with a class. <code>!important</code> is included to avoid specificity issues. Classes can also be used as mixins.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;pull-left&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;pull-right&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Clearfix</strong></p>
                                    <p>Clear the <code>float</code> on any element with the <code>.clearfix</code> class. Utilizes <a target="_blank" href="http://nicolasgallagher.com/micro-clearfix-hack/">the micro clearfix</a> as popularized by Nicolas Gallagher. Can also be used as a mixin.</p>
                                    <pre class="prettyprint">&lt;!-- Usage as a class --&gt;
&lt;div class=&quot;clearfix&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Screen reader content</strong></p>
                                    <p>Hide an element to all devices <strong>except screen readers</strong> with <code>.sr-only</code>. Necessary for following <a target="_blank" href="http://getbootstrap.com/getting-started/#accessibility">Bootstrap accessibility best practices</a>.</p>
                                    <pre class="prettyprint">&lt;a class=&quot;sr-only&quot; href=&quot;#content&quot;&gt;Skip to main content&lt;/a&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Background helper</strong></p>
                                    <p>Allows you to select the background as you want, use with <code>!important</code>. This also changed the font color.</p>
                                    <p>
                                        <span class="demo-box bg-midnight">.bg-midnight</span>
                                        <span class="demo-box bg-cloud">.bg-cloud</span>
                                        <span class="demo-box bg-silver">.bg-silver</span>
                                        <span class="demo-box bg-white bordered">.bg-white</span>
                                        <span class="demo-box bg-darknight">.bg-darknight</span>

                                        <span class="demo-box bg-primary">.bg-primary</span>
                                        <span class="demo-box bg-success">.bg-success</span>
                                        <span class="demo-box bg-info">.bg-info</span>
                                        <span class="demo-box bg-warning">.bg-warning</span>
                                        <span class="demo-box bg-danger">.bg-danger</span>
                                    </p>

                                    <pre class="prettyprint">&lt;div class=&quot;bg-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-danger&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-inverse&quot;&gt;...&lt;/div&gt;

&lt;!-- Also avilable --&gt;
&lt;div class=&quot;bg-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bg-blue&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Border Helper</strong></p>
                                    <p>Add class <code>.bordered</code> to give a border on any element. Default style <code>1px solid #E0E4E8</code>. See demo and available class below:</p>
                                    <p>
                                        <span class="demo-box bordered">.bordered</span>
                                        <span class="demo-box bordered-flat">.bordered-flat</span>
                                        <span class="demo-box bordered-top">.bordered-top</span>
                                        <span class="demo-box bordered-right bordered-left" title="bordered right and left">.bordered right left</span>
                                        <span class="demo-box bordered-bottom">.bordered-bottom</span>

                                        <span class="demo-box bordered-flat border-primary">.border-primary</span>
                                        <span class="demo-box bordered-flat border-green">.border-green</span>
                                        <span class="demo-box bordered-flat border-info">.border-info</span>
                                        <span class="demo-box bordered-flat border-orange">.border-orange</span>
                                        <span class="demo-box bordered-flat border-midnight">.border-midnight</span>
                                    </p>
                                    <pre class="prettyprint pre-scrollable nicescroll-off">&lt;div class=&quot;bordered&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;bordered-top&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on top only --&gt;
&lt;div class=&quot;bordered-right&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on right only --&gt;
&lt;div class=&quot;bordered-bottom&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on bottom only --&gt;
&lt;div class=&quot;bordered-left&quot;&gt;...&lt;/div&gt; &lt;!-- bordered on top left --&gt;
&lt;div class=&quot;bordered-flat&quot;&gt;...&lt;/div&gt; &lt;!-- bordered all, but 2px on bottom --&gt;

&lt;!-- Also can change border color --&gt;
&lt;div class=&quot;border-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-danger&quot;&gt;...&lt;/div&gt;

&lt;div class=&quot;border-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;border-blue&quot;&gt;...&lt;/div&gt;

&lt;!-- Disable border --&gt;
&lt;div class=&quot;no-border&quot;&gt;...&lt;/div&gt;</pre>
                                    <p><i class="fa fa-hand-o-up"></i> <small>use <code>.pre-scrollable .nicescroll-off</code></small></p>
                                </div><!--/cols -->

                                <div class="col-md-6">
                                    <p class="text-muted"><strong>Carets</strong></p>
                                    <p>Use carets to indicate dropdown functionality and direction. Note that the default caret will reverse automatically in <a href="buttons.php">dropup menus</a>.</p>
                                    <p><span class="caret"></span></p>
                                    <pre class="prettyprint">&lt;span class=&quot;caret&quot;&gt;&lt;/span&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Center content blocks</strong></p>
                                    <p>Set an element to <code>display: block</code> and center via <code>margin</code>. Available as a mixin and class.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;center-block&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Showing and hiding content</strong></p>
                                    <p>Force an element to be shown or hidden (<strong>including for screen readers</strong>) with the use of <code>.show</code> and <code>.hidden</code> classes. These classes use <code>!important</code> to avoid specificity conflicts, just like the <a href="helper-classes.php#helper-classes-floats">quick floats</a>. They are only available for block level toggling.</p>
                                    <p><code>.hide</code> is available, but it does not always affect screen readers and is <strong>deprecated</strong> as of Bootstrap v3.0.1. Use <code>.hidden</code> or <code>.sr-only</code> instead.</p>
                                    <p>Furthermore, <code>.invisible</code> can be used to toggle only the visibility of an element, meaning its <code>display</code> is not modified and the element can still affect the flow of the document.</p>
                                    <pre class="prettyprint">&lt;div class=&quot;show&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;hidden&quot;&gt;...&lt;/div&gt;</pre>
                                    <br>

                                    <p class="text-muted"><strong>Text helper</strong></p>
                                    <p>Allows you to select the color, sizing or Font style, use with <code>!important</code>.</p>
                                    <p class="text-primary">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-blue">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-warning">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-red">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <br>
                                    <p class="text-orange text-bold text-16">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-red text-linethrough">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>
                                    <p class="text-green text-italic text-sm">Consequat condimentum, fusce tincidunt, faucibus ante praesent</p>

                                    <pre class="prettyprint pre-scrollable">&lt;!-- Bootstrap color helper --&gt;
&lt;div class=&quot;text-primary&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-success&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-info&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-warning&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-danger&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-muted&quot;&gt;...&lt;/div&gt;
&lt;!-- Also avilable --&gt;
&lt;div class=&quot;text-darknight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-midnight&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-cloud&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-silver&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-white&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-teal&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-green&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-orange&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-red&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-blue&quot;&gt;...&lt;/div&gt;

&lt;!-- Sizing --&gt;
&lt;div class=&quot;text-sm&quot;&gt;...&lt;/div&gt; &lt;!-- .8em of parent font-size --&gt;
&lt;div class=&quot;text-lg&quot;&gt;...&lt;/div&gt; &lt;!-- 1.2em of parent font-size --&gt;
&lt;div class=&quot;text-xg&quot;&gt;...&lt;/div&gt; &lt;!-- 1.6em of parent font-size --&gt;
&lt;div class=&quot;text-16&quot;&gt;...&lt;/div&gt; &lt;!-- 16px font-size --&gt;
&lt;div class=&quot;text-24&quot;&gt;...&lt;/div&gt; &lt;!-- 24px font-size --&gt;
&lt;div class=&quot;text-32&quot;&gt;...&lt;/div&gt; &lt;!-- 32px font-size --&gt;
&lt;div class=&quot;text-48&quot;&gt;...&lt;/div&gt; &lt;!-- 48px font-size --&gt;
&lt;div class=&quot;text-64&quot;&gt;...&lt;/div&gt; &lt;!-- 64px font-size --&gt;

&lt;!-- Styling --&gt;
&lt;div class=&quot;text-bold&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-italic&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-underline&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-linethrough&quot;&gt;...&lt;/div&gt;
&lt;div class=&quot;text-lead&quot;&gt;...&lt;/div&gt; &lt;!-- 300 font-weight --&gt;
&lt;div class=&quot;text-nodecor&quot;&gt;...&lt;/div&gt; &lt;!-- no decoration --&gt;</pre>
                                    <p><i class="fa fa-hand-o-up"></i> <small>use <code>.pre-scrollable</code></small></p>
                                    <br>

                                    <p class="text-muted"><strong>Shadow helper</strong></p>
                                    <p>Give a nice shadow to any element. Use with <code>.shadow</code> or disable shadow with <code>no-shadow</code>.</p>
                                    <p>
                                        <span class="demo-box shadow bg-midnight">.shadow</span>
                                        <span class="demo-box shadow bordered-flat">.shadow</span>
                                        <span class="demo-box well no-shadow" title="A .well with no shadow">.no-shadow</span>
                                    </p>
                                    <br>

                                    <p class="text-muted"><strong>Corner helper</strong></p>
                                    <p>Give <code>4px</code> border radius on any element with <code>.corner</code>. See available class below:</p>
                                    <p>
                                        <span class="demo-box shadow corner bg-midnight">.corner</span>
                                        <span class="demo-box shadow corner-top bg-primary">.corner-top</span>
                                        <span class="demo-box shadow corner-bottom bg-danger">.corner-bottom</span>
                                        <span class="demo-box shadow corner-br corner-tl bg-success">.corner-tl/br</span>
                                        <span class="demo-box well no-corner" title="A .well with no corner">.no-corner</span>
                                    </p>
                                    <pre class="prettyprint">&lt;div class=&quot;corner&quot;&gt;...&lt;/div&gt; &lt;!-- corner all --&gt;
&lt;div class=&quot;corner-top&quot;&gt;...&lt;/div&gt; &lt;!-- top corner --&gt;
&lt;div class=&quot;corner-tr&quot;&gt;...&lt;/div&gt; &lt;!-- top right corner --&gt;
&lt;div class=&quot;corner-tl&quot;&gt;...&lt;/div&gt; &lt;!-- top left corner --&gt;
&lt;div class=&quot;corner-bottom&quot;&gt;...&lt;/div&gt; &lt;!-- bottom corner --&gt;
&lt;div class=&quot;corner-br&quot;&gt;...&lt;/div&gt; &lt;!-- bottom right corner --&gt;
&lt;div class=&quot;corner-bl&quot;&gt;...&lt;/div&gt; &lt;!-- bottom left corner --&gt;

&lt;!-- Disable corner --&gt;
&lt;div class=&quot;no-corner&quot;&gt;...&lt;/div&gt;</pre>
                                </div><!--/cols -->
                            </div><!--/row -->
                        </div><!-- /panel-body -->
                    </div><!-- /panel-helpclass -->




                    <div id="panel-resutils" class="panel panel-default">
                        <div class="panel-heading">
                            <div class="panel-actions">
                                <button data-refresh="#panel-resutils" title="refresh" class="btn-panel">
                                    <i class="fa fa-refresh"></i>
                                </button>
                                <button data-expand="#panel-resutils" title="expand" class="btn-panel">
                                    <i class="fa fa-expand"></i>
                                </button>
                                <button data-collapse="#panel-resutils" title="collapse" class="btn-panel">
                                    <i class="fa fa-caret-down"></i>
                                </button>
                                <button data-close="#panel-resutils" title="close" class="btn-panel">
                                    <i class="fa fa-times"></i>
                                </button>
                            </div><!-- /panel-actions -->
                            <h3 class="panel-title">Responsive Utilities</h3>
                        </div><!-- /panel-heading -->

                        <div class="panel-body">
                            <p class="lead">For faster mobile-friendly development, use these utility classes for showing and hiding content by device via media query. Also included are utility classes for toggling content when printed.</p>
                            <p>Try to use these on a limited basis and avoid creating entirely different versions of the same site. Instead, use them to complement each device's presentation. <strong>Responsive utilities are currently only available for block and table toggling.</strong> Use with inline and table elements is currently not supported.</p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th></th>
                                        <th>
                                        Extra small devices
                                        <small>Phones (&lt;768px)</small>
                                        </th>
                                        <th>
                                        Small devices
                                        <small>Tablets (&ge;768px)</small>
                                        </th>
                                        <th>
                                        Medium devices
                                        <small>Desktops (&ge;992px)</small>
                                        </th>
                                        <th>
                                        Large devices
                                        <small>Desktops (&ge;1200px)</small>
                                        </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th><code>.visible-xs</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-sm</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-md</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                    <tr>
                                        <th><code>.visible-lg</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        </tr>
                                    </tbody>
                                    <tbody>
                                    <tr>
                                        <th><code>.hidden-xs</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-sm</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-md</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-lg</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="panel-body">
                            <h4>Print classes</h4>
                            <p>Similar to the regular responsive classes, use these for toggling content for print.</p>
                        </div><!-- /panel-body -->
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th>Class</th>
                                        <th>Browser</th>
                                        <th>Print</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <th><code>.visible-print</code></th>
                                        <td class="is-hidden">Hidden</td>
                                        <td class="is-visible">Visible</td>
                                    </tr>
                                    <tr>
                                        <th><code>.hidden-print</code></th>
                                        <td class="is-visible">Visible</td>
                                        <td class="is-hidden">Hidden</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div><!-- /panel-resutils -->                </div><!--/content-body -->
            </div><!--/content -->

        </section><!--/content section -->
        

        <!-- side-right -->
        <aside class="side-right">
            <div class="module" data-toggle="niceScroll">
                <div class="chat-contact">
                    <h3 class="contact-heading">
                        <div class="btn-group pull-right">
                            <a href="helper-classes.php#" data-toggle="side-right">
                                <i class="fa fa-times text-sm"></i>
                            </a>
                        </div>
                        <i class="fa fa-group"></i> Hangouts 
                        <div class="btn-group">
                            <a href="helper-classes.php#" class="dropdown-toggle" data-toggle="dropdown">
                                <i class="fa fa-angle-down text-sm"></i>
                            </a>
                            <ul class="dropdown-menu" role="menu">
                                <li class="active"><a href="helper-classes.php#"><i class="fa fa-circle text-primary"></i> Online</a></li>
                                <li><a href="helper-classes.php#"><i class="fa fa-circle text-danger"></i> Offline</a></li>
                                <li><a href="helper-classes.php#"><i class="fa fa-circle text-warning"></i> Idle</a></li>
                                <li class="divider"></li>
                                <li><a href="helper-classes.php#"><i class="fa fa-circle text-midnight"></i> Disable</a></li>
                            </ul>
                        </div>
                    </h3><!-- /contact-heading -->

                    <div class="contact-body">
                        <ul class="contacts-list">
                            <li class="separate">Top friends</li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Phillip Morrison</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samuel Porter</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Kathy Reynolds</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Aaron James</a></li>
                            <li class="idle"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Teresa May</a></li>

                            <li class="separate">Teams</li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> John Doe</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Iin Triasneni</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Mahatma</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Lawrence Ramirez</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Samantha Jenkins</a></li>
                            <li class="disable"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Sarah Payne</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Justin Perry</a></li>

                            <li class="separate">Clients</li>
                            <li class="idle"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Rebecca Vargas</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Sean Carpenter</a></li>
                            <li class="idle"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Arthur Pearson</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Julie Jimenez</a></li>
                            <li class="idle"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Sandra Ramirez</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Nicholas Cole</a></li>
                            <li class="idle"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="idle" rel="tooltip-bottom"></i> Madison Hall</a></li>
                            <li class="offline"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="offline" rel="tooltip-bottom"></i> Alan Shaw</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Randy Mills</a></li>

                            <li class="separate">All</li>
                            <li class="disable"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Kenneth Soto</a></li>
                            <li class="disable"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="disable" rel="tooltip-bottom"></i> Harold James</a></li>
                            <li class="online"><a href="helper-classes.php#"><i class="fa fa-circle-o" title="online" rel="tooltip-bottom"></i> Paul Greene</a></li>
                        </ul><!-- /contacts-list -->
                    </div><!-- /contact-body -->
                </div><!-- /chat-contact -->

                <div class="chatbox">
                    <h3 class="chatbox-heading">
                        <a data-toggle="chatbox-close" href="helper-classes.php#" class="pull-right text-sm text-silver"><i class="fa fa-times"></i></a>
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
        <a rel="to-top" href="helper-classes.php#top"><i class="fa fa-arrow-up"></i></a>
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
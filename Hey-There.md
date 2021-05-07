
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Let’s Scrape Twitter! (w/ Python) &#8212; My Jupyter Book</title>
    
  <link rel="stylesheet" href="_static/css/index.f658d18f9b420779cfdf24aa0a7e2d77.css">

    
  <link rel="stylesheet"
    href="_static/vendor/fontawesome/5.13.0/css/all.min.css">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="_static/vendor/fontawesome/5.13.0/webfonts/fa-solid-900.woff2">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="_static/vendor/fontawesome/5.13.0/webfonts/fa-brands-400.woff2">

    
      
  <link rel="stylesheet"
    href="_static/vendor/open-sans_all/1.44.1/index.css">
  <link rel="stylesheet"
    href="_static/vendor/lato_latin-ext/1.44.1/index.css">

    
    <link rel="stylesheet" href="_static/sphinx-book-theme.e7340bb3dbd8dde6db86f25597f54a1b.css" type="text/css" />
    <link rel="stylesheet" href="_static/pygments.css" type="text/css" />
    <link rel="stylesheet" type="text/css" href="_static/togglebutton.css" />
    <link rel="stylesheet" type="text/css" href="_static/copybutton.css" />
    <link rel="stylesheet" type="text/css" href="_static/mystnb.css" />
    <link rel="stylesheet" type="text/css" href="_static/sphinx-thebe.css" />
    <link rel="stylesheet" type="text/css" href="_static/panels-main.c949a650a448cc0ae9fd3441c0e17fb0.css" />
    <link rel="stylesheet" type="text/css" href="_static/panels-variables.06eb56fa6e07937060861dad626602ad.css" />
    
  <link rel="preload" as="script" href="_static/js/index.d3f166471bb80abb5163.js">

    <script id="documentation_options" data-url_root="./" src="_static/documentation_options.js"></script>
    <script src="_static/jquery.js"></script>
    <script src="_static/underscore.js"></script>
    <script src="_static/doctools.js"></script>
    <script src="_static/language_data.js"></script>
    <script src="_static/togglebutton.js"></script>
    <script src="_static/clipboard.min.js"></script>
    <script src="_static/copybutton.js"></script>
    <script >var togglebuttonSelector = '.toggle, .admonition.dropdown, .tag_hide_input div.cell_input, .tag_hide-input div.cell_input, .tag_hide_output div.cell_output, .tag_hide-output div.cell_output, .tag_hide_cell.cell, .tag_hide-cell.cell';</script>
    <script src="_static/sphinx-book-theme.7d483ff0a819d6edff12ce0b1ead3928.js"></script>
    <script async="async" src="https://unpkg.com/thebelab@latest/lib/index.js"></script>
    <script >
        const thebe_selector = ".thebe"
        const thebe_selector_input = "pre"
        const thebe_selector_output = ".output"
    </script>
    <script async="async" src="_static/sphinx-thebe.js"></script>
    <link rel="index" title="Index" href="genindex.html" />
    <link rel="search" title="Search" href="search.html" />
    <link rel="next" title="Overview" href="start/overview.html" />

    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="docsearch:language" content="en" />



  </head>
  <body data-spy="scroll" data-target="#bd-toc-nav" data-offset="80">
    

    <div class="container-xl">
      <div class="row">
          
<div class="col-12 col-md-3 bd-sidebar site-navigation show" id="site-navigation">
    
        <div class="navbar-brand-box">
<a class="navbar-brand text-wrap" href="index.html">
  
  
  <h1 class="site-logo" id="site-title">My Jupyter Book</h1>
  
</a>
</div><form class="bd-search d-flex align-items-center" action="search.html" method="get">
  <i class="icon fas fa-search"></i>
  <input type="search" class="form-control" name="q" id="search-input" placeholder="Search this book..." aria-label="Search this book..." autocomplete="off" >
</form>
<nav class="bd-links" id="bd-docs-nav" aria-label="Main navigation">
    <ul class="nav sidenav_l1">
 <li class="toctree-l1 current active">
  <a class="reference internal" href="#">
   Let’s Scrape Twitter! (w/ Python)
  </a>
 </li>
</ul>
<p class="caption collapsible-parent">
 <span class="caption-text">
  Get started
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="start/overview.html">
   Overview
  </a>
 </li>
</ul>
<p class="caption collapsible-parent">
 <span class="caption-text">
  Other Scraping Options
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="other/BS_Requests.html">
   Requests and BeautifulSoup
  </a>
 </li>
</ul>
<p class="caption collapsible-parent">
 <span class="caption-text">
  Twitter API
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="api/What_API.html">
   What is an Application Programming Interface (API)
  </a>
 </li>
 <li class="toctree-l1 collapsible-parent">
  <a class="reference internal" href="api/Python_info.html">
   Some presentation notes
  </a>
  <ul class="collapse-ul">
   <li class="toctree-l2">
    <a class="reference internal" href="api/twitter_api_steps.html">
     Setting Up Twitter API
    </a>
   </li>
  </ul>
  <i class="fas fa-chevron-down">
  </i>
 </li>
</ul>
<p class="caption collapsible-parent">
 <span class="caption-text">
  Demos
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="demos/beautifulsoup_demo.html">
   Scraping Counter-Currents
  </a>
 </li>
</ul>
<p class="caption collapsible-parent">
 <span class="caption-text">
  Reference
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference external" href="https://jupyterbook.org/cite.html">
   Cite Jupyter Book
   <i class="fas fa-external-link-alt">
   </i>
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference external" href="https://bregreen.github.io/">
   My Personal Website
   <i class="fas fa-external-link-alt">
   </i>
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference external" href="https://developer.twitter.com/en">
   Developer Twitter
   <i class="fas fa-external-link-alt">
   </i>
  </a>
 </li>
</ul>

</nav> <!-- To handle the deprecated key -->

<div class="navbar_extra_footer">
  Powered by <a href="https://jupyterbook.org">Jupyter Book</a>
</div>

</div>


          


          
<main class="col py-md-3 pl-md-4 bd-content overflow-auto" role="main">
    
    <div class="topbar container-xl fixed-top">
    <div class="topbar-contents row">
        <div class="col-12 col-md-3 bd-topbar-whitespace site-navigation show"></div>
        <div class="col pl-md-4 topbar-main">
            
            <button id="navbar-toggler" class="navbar-toggler ml-0" type="button" data-toggle="collapse"
                data-toggle="tooltip" data-placement="bottom" data-target=".site-navigation" aria-controls="navbar-menu"
                aria-expanded="true" aria-label="Toggle navigation" aria-controls="site-navigation"
                title="Toggle navigation" data-toggle="tooltip" data-placement="left">
                <i class="fas fa-bars"></i>
                <i class="fas fa-arrow-left"></i>
                <i class="fas fa-arrow-up"></i>
            </button>
            
            
<div class="dropdown-buttons-trigger">
    <button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn" aria-label="Download this page"><i
            class="fas fa-download"></i></button>

    <div class="dropdown-buttons">
        <!-- ipynb file if we had a myst markdown file -->
        
        <!-- Download raw file -->
        <a class="dropdown-buttons" href="_sources/Hey-There.ipynb"><button type="button"
                class="btn btn-secondary topbarbtn" title="Download source file" data-toggle="tooltip"
                data-placement="left">.ipynb</button></a>
        <!-- Download PDF via print -->
        <button type="button" id="download-print" class="btn btn-secondary topbarbtn" title="Print to PDF"
            onClick="window.print()" data-toggle="tooltip" data-placement="left">.pdf</button>
    </div>
</div>

            <!-- Source interaction buttons -->


            <!-- Full screen (wrap in <a> to have style consistency -->
            <a class="full-screen-button"><button type="button" class="btn btn-secondary topbarbtn" data-toggle="tooltip"
                    data-placement="bottom" onclick="toggleFullScreen()" aria-label="Fullscreen mode"
                    title="Fullscreen mode"><i
                        class="fas fa-expand"></i></button></a>

            <!-- Launch buttons -->

<div class="dropdown-buttons-trigger">
    <button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn"
        aria-label="Launch interactive content"><i class="fas fa-rocket"></i></button>
    <div class="dropdown-buttons">
        
        <a class="binder-button" href="https://mybinder.org/v2/gh/executablebooks/jupyter-book/master?urlpath=tree/Hey-There.ipynb"><button type="button"
                class="btn btn-secondary topbarbtn" title="Launch Binder" data-toggle="tooltip"
                data-placement="left"><img class="binder-button-logo"
                    src="_static/images/logo_binder.svg"
                    alt="Interact on binder">Binder</button></a>
        
        
        
        
    </div>
</div>

        </div>

        <!-- Table of contents -->
        <div class="d-none d-md-block col-md-2 bd-toc show">
            
        </div>
    </div>
</div>
    <div id="main-content" class="row">
        <div class="col-12 col-md-9 pl-md-3 pr-md-0">
        
              <div>
                
  <div class="section" id="let-s-scrape-twitter-w-python">
<h1>Let’s Scrape Twitter! (w/ Python)<a class="headerlink" href="#let-s-scrape-twitter-w-python" title="Permalink to this headline">¶</a></h1>
<p><strong>A demo by <a class="reference external" href="https://bregreen.github.io/">Breanna E. Green </a> // Powered by <a class="reference external" href="https://jupyterbook.org/">Jupyter Book</a></strong></p>
<p>This webpage contains materials for a simple introduction to scraping content from Twitter. I created it present to colleagues and friends at Cornell in 2021 Spring (so if you are seeing this many moons in the future… brace yourself for this relic). A quick snippet about me – I am a PhD Student in the <a class="reference external" href="https://infosci.cornell.edu/research">Information Science</a> Department who’s main research interest is how activist and extremist ideologies are developed and manifested online, particularly using social media.</p>
 <img src="logo.PNG" alt="Cartoon version of B. E. Green" width="200"/>
<p><strong>How are we going to do this?</strong></p>
<p>Let’s get the core information out of the way. We will breeze through most of that (hopefully in about 5-10 minutes). Then we can talk through some demos and answer really good questions sent to me.</p>
<p>These questions/topics included things like:</p>
<ul class="simple">
<li><p>How to gather tweets from different users?</p>
<ul>
<li><p>How many to gather from each person? Are there norms/conventions in research for this? Without a specific question on the topic (i.e., I don’t think I really care about how many we get), what is “standard practice”?</p></li>
<li><p>Which tweets to gather? Random selection, most recent, most liked, etc? Again, absent a more specific question, are there norms/conventions for this?</p></li>
</ul>
</li>
<li><p>How to diagnose political ideology?</p>
<ul>
<li><p>How do we determine each user’s political ideology, on some scale from “Very Liberal” to “Very Conservative”?</p></li>
</ul>
</li>
<li><p>Descriptive stats on tweets?</p>
<ul>
<li><p>Frequency of words like “we, us, our, ours”</p></li>
</ul>
</li>
</ul>
<p><strong>Acknowledgments</strong>
I only learned how to develop this page after seeing the magnificent course materials of <a class="reference external" href="https://github.com/melaniewalsh/Intro-Cultural-Analytics">Melanine Walsh</a>, who themselves cite the works of <a class="reference external" href="https://github.com/laurenfklein/emory-qtm340">Lauren Klein</a>, <a class="reference external" href="https://mimno.infosci.cornell.edu/info3350/">David Mimno</a>, and <a class="reference external" href="https://github.com/aparrish/rwet">Allison Parrish</a>. Many, many thanks for such a beautiful and informative site!</p>
<p>Second, many thanks to friends in the <a class="reference external" href="http://www.kroschlab.com/">THE SOCIAL PERCEPTION AND INTERGROUP (IN)EQUALITY LAB</a> for whom I motivated to work on this! Otherwise, it might have been a powerpoint. <em>Crowd boos in dissatisfaction.</em></p>
<div class="toctree-wrapper compound">
</div>
<div class="toctree-wrapper compound">
</div>
<div class="toctree-wrapper compound">
</div>
<div class="toctree-wrapper compound">
</div>
<div class="toctree-wrapper compound">
</div>
<div class="toctree-wrapper compound">
</div>
</div>

    <script type="text/x-thebe-config">
    {
        requestKernel: true,
        binderOptions: {
            repo: "binder-examples/jupyter-stacks-datascience",
            ref: "master",
        },
        codeMirrorConfig: {
            theme: "abcdef",
            mode: "python"
        },
        kernelOptions: {
            kernelName: "python3",
            path: "./."
        },
        predefinedOutput: true
    }
    </script>
    <script>kernelName = 'python3'</script>

              </div>
              
        
        <div class='prev-next-bottom'>
            
    <a class='right-next' id="next-link" href="start/overview.html" title="next page">Overview</a>

        </div>
        
        </div>
    </div>
    <footer class="footer mt-5 mt-md-0">
    <div class="container">
      <p>
        
          By The Jupyter Book community<br/>
        
            &copy; Copyright 2020.<br/>
      </p>
    </div>
  </footer>
</main>


      </div>
    </div>

    
  <script src="_static/js/index.d3f166471bb80abb5163.js"></script>


    
  </body>
</html>

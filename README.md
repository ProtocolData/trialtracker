<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links

reference file here https://gitlab.unige.ch/Joakim.Tutt/Best-README-Template/-/tree/master
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<br />
<p align="center">
<!--   <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
 -->
  <h3 align="center">Trial Tracker</h3>

  <p align="center">
    Improving cancer research with data!


  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Cancer is one of the leading causes of death worldwide. The way we test and approve new treatments is through clinical trials.  But 97% of cancer trials 
    <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6409418/">fail</a>, 
    driven by inability to 
    <a href="https://pubmed.ncbi.nlm.nih.gov/34823582/">recruit</a>
    enough patients.
And yet many patients are routinely 
    <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3980490/">excluded</a> 
    from trials, including minority groups who are most affected by the disease.
    <br />
    <br />

The key to solving these problems is in changing how we design clinical trials. Regulatory requirements for clinical trial registration became required in 2017, making semi-structured trial protocol data available on clinicaltrials.gov. Today, this is not being systematically used in trial design and patient recruitment decisions in Oncology. A few goals of this project:

    
<br /> - Explore clinical trial data from clinicaltrials.gov
    <br /> - Develop a method to extract structured core eligibility criteria for cancer trials (extending work  
    <a href="https://pubmed.ncbi.nlm.nih.gov/30753493/">here</a>  and 
    <a href="https://arxiv.org/abs/2006.07296">here</a>)
    <br /> - Combine extracted criteria with real-world oncology data to evaluate the impact of eligibility criteria on trial racial diversity (extending work 
    <a href="https://www.nature.com/articles/s41586-021-03430-5">here</a> by incorporating race data)
    <br /> - Generate a diversity rating for each clinical trial


### Built With
Technologies and methods used to build this project!
* [Python](https://www.python.org/)
* [Golang](https://go.dev/)
* [Named Entity Recognition and Named Entity Linking](https://arxiv.org/abs/2006.07296)



<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow the steps below.

### Prerequisites

Get up and running with conda.  Given the many dependencies of this project, we use conda as a package/environment manager to make sure we're running things in the same environment and that nothing breaks :)


### Installation

1. Clone the repo
```sh
git clone https://github.com/zfx0726@gmail.com/trialtracker.git
```
2. Navigate into the trialtracker project directory and recreate the conda environment.
```sh
conda env create --file=trialtrackerenv_py36.yaml
```
3. Activate conda python environment
```sh
conda activate trialtrackerenv_py36
```



 <!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

 -->

<!-- ROADMAP -->
<!-- ## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).
 -->


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See 
<a href="https://github.com/zfx0726/trialtracker/blob/main/LICENSE">`LICENSE`</a> 
for more information.



<!-- CONTACT -->
## Contact

<!-- Forrest Xiao - [@your_twitter](https://twitter.com/your_username) - email@example.com -->
Forrest Xiao - zfx0726@gmail.com



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)
 -->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->

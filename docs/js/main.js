"use strict";
$(window).load(function() {
  //Preloader
  /** Loader */
  var loader = $(".loader");
  var wHeight = $(window).height();
  var wWidth = $(window).width();
  var o = 0;

  loader.css({
    top: wHeight / 2 - 2.5,
    left: wWidth / 2 - 200
  });

  do {
    loader.animate(
      {
        width: o
      },
      10
    );
    o += 3;
  } while (o <= 400);
  if (o === 402) {
    loader.animate({
      left: 0,
      width: "100%"
    });
    loader.animate({
      top: "0",
      height: "100vh"
    });
  }

  setTimeout(function() {
    $(".loader-wrapper").fadeOut("fast");
    loader.fadeOut("fast");
  }, 3500);

  // Portfolio isotope
  if ($(".isotope_items").length) {
    var $container = $(".isotope_items");
    $container.isotope();

    $(".portfolio_filter ul li").on("click", function() {
      $(".portfolio_filter ul li").removeClass("select-cat");
      $(this).addClass("select-cat");
      var selector = $(this).attr("data-filter");
      $(".isotope_items").isotope({
        filter: selector,
        animationOptions: {
          duration: 750,
          easing: "linear",
          queue: false
        }
      });
      return false;
    });
  }
}); // window load end

$(document).ready(function() {
  //SMOOTH SCROLL
  $(document).on("scroll", onScroll);
  $('a[href^="#"]').on("click", function(e) {
    e.preventDefault();
    $(document).off("scroll");

    $("a").each(function() {
      $(this).removeClass("active");
      if ($(window).width() < 768) {
        $(".nav-menu").slideUp();
      }
    });

    $(this).addClass("active");

    var target = this.hash,
      menu = target;
    target = $(target);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: target.offset().top + 2
        },
        500,
        "swing",
        function() {
          window.location.hash = target.selector;
          $(document).on("scroll", onScroll);
        }
      );
  });

  function onScroll(event) {
    if ($("#home").length) {
      var scrollPos = $(document).scrollTop();
      $("nav ul li a").each(function() {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (
          refElement.position().top <= scrollPos &&
          refElement.position().top + refElement.height() > scrollPos
        ) {
          $("nav ul li a").removeClass("active");
          currLink.addClass("active");
        } else {
          currLink.removeClass("active");
        }
      });
    }
  }

  //Navbar show/hide
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();
    var homeheight = $(".home").height() - 86;

    if (scroll > homeheight) {
      $("nav").slideDown(150);
    } else {
      $("nav").slideUp(150);
    }
  });

  // Responsive menu
  $(".responsive").on("click", function(e) {
    $(".nav-menu").slideToggle();
  });

  // Home page height
  function centerInit() {
    var hometext = $(".home");

    hometext.css({
      height: $(window).height() + "px"
    });
  }
  centerInit();
  $(window).resize(centerInit);

  //Typed js
  if ($(".element").length) {
    $(".element").each(function() {
      $(this).typed({
        strings: [$(this).data("text1"), $(this).data("text2")],
        loop: $(this).data("loop") ? $(this).data("loop") : false,
        backDelay: $(this).data("backdelay") ? $(this).data("backdelay") : 2000,
        typeSpeed: 10
      });
    });
  }

  // Owl carousel js
  var owlcar = $(".owl-carousel");
  if (owlcar.length) {
    owlcar.each(function() {
      var $owl = $(this);
      var itemsData = $owl.data("items");
      var autoPlayData = $owl.data("autoplay");
      var paginationData = $owl.data("pagination");
      var navigationData = $owl.data("navigation");
      var stopOnHoverData = $owl.data("stop-on-hover");
      var itemsDesktopData = $owl.data("items-desktop");
      var itemsDesktopSmallData = $owl.data("items-desktop-small");
      var itemsTabletData = $owl.data("items-tablet");
      var itemsTabletSmallData = $owl.data("items-tablet-small");
      $owl.owlCarousel({
        items: itemsData,
        pagination: paginationData,
        navigation: navigationData,
        autoPlay: autoPlayData,
        stopOnHover: stopOnHoverData,
        navigationText: ["<", ">"],
        itemsCustom: [
          [0, 1],
          [500, itemsTabletSmallData],
          [710, itemsTabletData],
          [992, itemsDesktopSmallData],
          [1199, itemsDesktopData]
        ]
      });
    });
  }
}); // document ready end

// Countdown/progress bar
function getDaysRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  var days = Math.floor(t / (1000 * 60 * 60 * 24));
  return days;
}
function getTimeSince(starttime) {
  var t = Date.parse(new Date()) - Date.parse(starttime);
  var days = Math.floor(t / (1000 * 60 * 60 * 24));
  var weeks = Math.floor(days / 7);
  var daysOfWeek = days % 7;
  return {
    weeks: weeks,
    days: daysOfWeek
  };
}

function getPercentage(starttime, endtime) {
  startDate = Date.parse(starttime);
  endDate = Date.parse(endtime);
  var diff = 0;
  var totalDays;
  var decimal, percentage;
  diff = endDate - startDate;
  totalDays = Math.floor(diff / (1000 * 60 * 60 * 24));

  var progressDiff = Date.parse(new Date()) - Date.parse(starttime);
  var progressDays = Math.floor(progressDiff / (1000 * 60 * 60 * 24));

  decimal = progressDays / totalDays;

  percentage = Math.floor(decimal * 100);
  return percentage;
}

var startDate = "2019-09-11";
var endDate = "2019-12-19";

var timeGone = getTimeSince(startDate);
var daysLeft = getDaysRemaining(endDate);
var percentComplete = getPercentage(startDate, endDate);

document.getElementById("progress-bar").style.width =
  percentComplete.toString() + "%";

var countdown = document.getElementById("countdown");
countdown.innerHTML = percentComplete.toString() + "% " + " complete";

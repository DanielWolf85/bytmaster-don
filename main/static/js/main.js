$(document).ready(function() {

	// для выпадающего списка мобильного меню

	$('.menu-item-54').click(function() {
		$('.menu-item-54 > .sub-menu').toggleClass('sub-menu_active');
	})

	// плавный скролл до лябого якоря
	$(function(){
	    $("a[href^='#']").click(function(){
            var _href = $(this).attr("href");
            $("html, body").animate({scrollTop: $(_href).offset().top+"px"});
            return false;
	  	});
	});


	// кнопка наверх
	var goTopButton = function() {
		var goButtonShow = 500,
			fadeInTime = 400,
			fadeOutTime = 400,
			goTop = $('#to-top');
		$(window).on('scroll', function() {
			if ($(window).scrollTop() >= goButtonShow) {
				goTop.fadeIn(fadeInTime);
			} else {
				goTop.fadeOut(fadeOutTime);
			}
		});
	}

	goTopButton();

});



// Мобильное меню
function mobile_menu_on() {
	$(".mobile_nav").removeClass("mobile_disabled");
	$(".mobile_nav").addClass("mobile_enabled");
}

function mobile_menu_off() {
	$(".mobile_nav").removeClass("mobile_enabled");
	$(".mobile_nav").addClass("mobile_disabled");
}

// function drop_sub_menu(class_el) {
// 	$('.' + class_el + ' > .sub-menu').css('display', 'block');
// }


// Обратный звонок
function back_call_on() {
	$(".back-call").removeClass("back-call__off");
	$(".back-call").addClass("back-call__active");
	$('.overlay').css('display', 'block');
}

function back_call_off() {
	$(".back-call").removeClass("back-call__active");
	$(".back-call").addClass("back-call__off");
	$('.overlay').css('display', 'none');
}


// Заявка с сайта
function zayavka_on() {
	$(".zayavka").removeClass("zayavka__off");
	$(".zayavka").addClass("zayavka__active");
	$('.overlay').css('display', 'block');
}

function zayavka_off() {
	$(".zayavka").removeClass("zayavka__active");
	$(".zayavka").addClass("zayavka__off");
	$('.overlay').css('display', 'none');
}




$(document).ready(function() {

	// Team slider
	$('.team-slider').slick({
		//infinite: true,
		autoplay: true,
		autoplaySpeed: 2000,
		slidesToShow: 3,
		slidesToScroll: 1,
		responsive: [
			{
				breakpoint: 768,
				settings: {
					slidesToShow: 2
				}
			},
			{
				breakpoint: 480,
				settings: {
					slidesToShow: 1,
					arrows: false
				}
			}
		]
	});


	// Review slider
	$('.reviews-body').slick({
		autoplay: true,
		autoplaySpeed: 6000,
		slidesToShow: 1,
		slidesToScroll: 1,
		responsive: [
			{
				breakpoint: 768,
				settings: {
					arrows: false
				}
			}
		]
	});

})






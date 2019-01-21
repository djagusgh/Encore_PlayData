// 이벤트 등록
$(document).on('scroll', scrollHandler);
$('#about-btn').on('click', scrollAbout);
$('#contact-btn').on('click', scrollContact);

scrollHandler();

function scrollHandler(){
	//console.log("현재 스크롤한 부분까지의 높이 =======",$(window).height() + $(window).scrollTop());
	// console.log("navbar 현재 위치 ======", $('.navbar').offset().top);

	// pt.1
	// 'header' 섹션에 있을 때는 네비게이션바의 메뉴가 흰색 
	// 'about', 'contact' 섹션으로 이동하면 폰트 #4A4A4A로 변경!
	if($('.navbar').offset().top > $('.header').offset().top + $('.header').height()){
		$('#about-btn').css('color', '#4A4A4A');
		$('#contact-btn').css('color', '#4A4A4A');
	} else {
		$('#about-btn').css('color', 'white');
		$('#contact-btn').css('color', 'white');
	}

	// pt.3
	// 스크롤을 해서 각 섹션에 다다르면 해당 섹션의 'vertical-center' 
	// 요소가 보이면서 정가운데로 1초 이내에 서서히 올라오도록

	$('section').each(function(){
		// $(window).height() + $(window).scrollTop() : 현재 스크롤한 부분까지의 높이
		if( $(window).height() + $(window).scrollTop() >= Math.floor($(this).offset().top + $(this).height()) ){
			$(this).find('.vertical-center').animate({opacity : '1', top: '0px'}, 1000);

			// pt.4
			// 'About' 섹션에 나의 스킬 여섯 개가 나열되어 있습니다. 
			// 'About' 섹션에 다다랐을 때 해당 스킬의 퍼센티지(%)만큼 파란 막대기가 서서히 색칠되도록 해주세요.
			if (this === $('.about')[0]){
				var idx = 0;
				$('.bar .percentage').each(function(){
					$('.inner-bar').eq(idx).animate({width : $(this).text()}, 1500);
					idx += 1;
				})
			} // 안쪽 if
		} // 바깥 if
	})
} // scrollHandler

// pt.2

function scrollAbout(){
	// click 시 about section 으로 이동
	$('html, body').animate({scrollTop: $('.about').offset().top + $('.about').height() - $(window).height()}, 1000);
}

function scrollContact(){
	// click 시 contact section 으로 이동 
	$('html, body').animate({scrollTop: $('.contact').offset().top + $('.contact').height() - $(window).height()}, 1000);
	
}
function scrollHandler() {

	if ($(window).scrollTop > $('.about').position().top){
		$('.menu-right button').css('color', '#4a4a4a');

		// pt.4
		$('.skill').each(function(){
			var skill = $(this);
			var percentage = skill.find('.percentage').text();
			skill.find('.inner-bar').animate({width: percentage}, 1200);
		})

	} else {
		$('.menu-right button').css('color', 'white');
	}

	// 각 섹션을 보고
	// 현재 스크롤 위치가 그 섹션보다 아래에 있으면
	// 그 세션에 vertical-center를 animate 시켜라!

	$('section').each(function(){
		if ($(window).scrollTop() >= $(this).position().top){
			$(this).find('.vertical-center').animate({top: '0', opacity : '1'}, 800);
		}
	})

}

$(window).on('scroll', scrollHandler);

// 처음 페이지가 로딩됐을 때
scrollHandler();

// 섹션 스크롤
$('.menu-right button').on('click', function() {
	var id = $(this).attr('id');
	if (id == 'about-btn'){
		$('html, body').animate({scrollTop: $('.about').position().top}, 1000);
	} else if (id == 'contact-btn'){
		$('html, body').animate({scrollTop: $('.contact').position().top}, 1000);
	}
})


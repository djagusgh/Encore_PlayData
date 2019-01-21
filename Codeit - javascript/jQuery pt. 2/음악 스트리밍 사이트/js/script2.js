
scrollHandler();
$(window).on('scroll', scrollHandler);

// 버튼 클릭 시 화면 맨 위로 스크롤 되면서 버튼 사라짐
$('.to-top-btn').on('click', function(){
	$('html, body').animate({scrollTop: 0}, 500);
	$('.to-top-btn').fadeOut(1000);
});


// for문 대신 each로 구현
function scrollHandler() {
	// 웹 페이지 전체의 높이
	var scrollHeight = $(document).height();
	// 현재 스크롤한 부분까지의 높이
	var currentScroll = $(window).scrollTop() + $(window).height();

 	$('.playlist').each(function(){
 		var centerPosition = $(this).offset().top + $(this).height()*0.5;
 		if (currentScroll > centerPosition){
 			$(this).animate({opacity: '1'}, 1000);
 		}
 	})

 	if(scrollHeight === Math.floor(currentScroll)){
 		$('.to-top-btn').fadeIn(1000);
 	} else{
 		$('.to-top-btn').fadeOut(1000);
 	}
}

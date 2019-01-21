// 'playlist'가 브라우저에 반 이상 걸치면 opacity가 서서히 1로 바뀌어야
var playlists = $('.playlist');
var playListCenters = makePlayListCenters();

scrollHandler();
$(window).on('scroll', scrollHandler);


function makePlayListCenters() { 
	// 각 playlist의 중심들을 array에 집어넣기
	// scrollHandler 함수 반복문 내에서도 구할 수 있지만, scroll 내릴 때마다 계속 중심 위치 계산해야.. -> 비효율 
	var playListCenters = [];
	for (var i = 0; i < playlists.length; i++){
		var playListCenter = playlists.eq(i).offset().top + playlists.eq(i).height()*0.5;
		playListCenters.push(playListCenter);
	}
	return playListCenters;
}

function scrollHandler() {
	// 스크롤에 따라 playlist의 opacity 변경
	var currentScroll = $(window).scrollTop() + $(window).height();
	// 'playlist'가 브라우저에 반 이상 걸치면 opacity가 서서히 1로 바뀌어야
	for (var i = 0; i < playlists.length; i++){
		if (currentScroll > playListCenters[i]){
			playlists.eq(i).animate({opacity: '1'}, 1000);
		}
	}
}



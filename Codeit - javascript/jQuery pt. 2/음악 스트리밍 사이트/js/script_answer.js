
scrollHandler();
$(window).on('scroll', scrollHandler);


function scrollHandler() {
	var windowBottom = $(window).scrollTop() + $(window).height();

	// 모든 playlist를 하나씩 살펴보고
	// 그 playlist의 중간 지점의 좌표가 windowBottom 보다 작으면
	// 그 playlist를 보이게 한다!

	// 1. for문 사용

	// var playlists = $('.playlist');
	// for (var i = 0; i < playlists.length; i++){
	// 	var playlist = $(playlists[i]);
	// 	var playlistHalf = playlist.position().top + playlist.outerHeight()/2;

	// 	if (playlistHalf < windowBottom) {
	// 		playlist.animate({'opacity' : 1}, 1500);
	// 	}
	// }

	// 2. each 사용
	$('.playlist').each(function(){
		var playlist = $(this);
		var playlistHalf = playlist.position().top + playlist.outerHeight()/2;

		if (playlistHalf < windowBottom) {
			playlist.animate({'opacity' : '1'}, 1500);
		}

	})

}


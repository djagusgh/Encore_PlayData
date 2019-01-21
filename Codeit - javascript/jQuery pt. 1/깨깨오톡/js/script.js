// 이벤트 등록
$('#send').on('click', sendMessage);

function sendMessage(){
	// textarea의 값을 받아옴 
	var sendContent = $('.text-box textarea').val();
	// 마지막 bubble class의 아래에 my-bubble class를 추가함
	if (sendContent !== ""){
		$('.bubble:last-child').after("<div class='my-bubble bubble'>" + sendContent + "</div>");
		// 해설
		// $('.chatbox').append("<div class='my-bubble bubble'>" + sendContent + "</div>");
	}
	
	// 메시지 전송시 textarea 빈칸 만들기

	$('.text-box textarea').val('');
	
}
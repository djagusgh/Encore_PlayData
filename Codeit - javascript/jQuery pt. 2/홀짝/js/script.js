  // 이벤트 등록
  $('button').on('click', function(event){
  	var buttonId = event.currentTarget.id;

  	if (buttonId === 'even-btn'){
  		$('.card').each(function(){
  		var num = Number($(this).text()); // 각각의 숫자
  		$(this).removeClass('selected');
  		if (num % 2 == 0){
  		 	$(this).addClass('selected');
  		 }
  	})

  	} else if(buttonId === 'odd-btn'){
		$('.card').each(function(){
  		var num = Number($(this).text()); // 각각의 숫자
  		$(this).removeClass('selected');
  		if (num % 2 == 1){
  		 	$(this).addClass('selected');
  		 }
  		})  		
  	} // else if
  	
  }) // $('button').on


  // 해설
  $('#even-btn').on('click', function(){
    $('.card').removeClass('selected');
    $('.card').each(function(){
      if (Number($(this).text()) % 2 === 0) {
        console.log($(this).text());
        $(this).addClass('selected');
      }
    })
  })


  $('#odd-btn').on('click', function(){
    $('.card').removeClass('selected');
    $('.card').each(function(){
      if (Number($(this).text()) % 2 === 1) {
        console.log($(this).text());
        $(this).addClass('selected');
      }
    })
  })
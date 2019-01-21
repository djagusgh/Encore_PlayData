
// 청기 내려
$('#btn1').on('click', function(){
  $('.flag.blue').addClass("down");
  // 1초 뒤에 깃발 올라오도록!
  setTimeout(function(){
    $('.flag.blue').removeClass("down");
  }, 1000);

});

// 청기 내리지 말고 백기 내려
$('#btn2').on('click', function(){
  $('.flag.white').addClass("down");
  // 1초 뒤에 깃발 올라오도록!
  setTimeout(function(){
    $('.flag.white').removeClass("down");
  }, 1000);


});

// 점선 청기 내려
$('#btn3').on('click', function(){
  $('.flag.blue.dot').addClass("down");
  // 1초 뒤에 깃발 올라오도록!
  setTimeout(function(){
    $('.flag.blue.dot').removeClass("down");
  }, 1000);
});




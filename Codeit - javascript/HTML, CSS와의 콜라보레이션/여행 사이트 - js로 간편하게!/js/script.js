// 이벤트 핸들링
    $('#home').on('click', clickHome); // clickHome() -> x 
    $('#seoul').on('click', clickSeoul);
    $('#tokyo').on('click', clickTokyo);
    $('#paris').on('click', clickParis);

    $('#photo').on('mouseenter', mouseEnterPhoto);
    $('#photo').on('mouseleave', mouseLeavePhoto);

    // 키보드 이벤트
    $(document).on('keydown', processKeyEvent); // document 페이지 전체


    // 사진을 바꿔주는 함수
    function clickHome() {
      // document.getElementById('photo').src = 'images/home.png';
      // jQuery 사용 문법
      $('#photo').attr('src', 'images/home.png');

      $('#home').css('font-weight', 'bold');
      $('#seoul').css('font-weight', 'normal');
      $('#tokyo').css('font-weight', 'normal');
      $('#paris').css('font-weight', 'normal');
    }

    function clickSeoul() {
      // document.getElementById('photo').src = 'images/seoul.png';
      // jQuery 사용 문법
      $('#photo').attr('src', 'images/seoul.png');

      $('#home').css('font-weight', 'normal');
      $('#seoul').css('font-weight', 'bold');
      $('#tokyo').css('font-weight', 'normal');
      $('#paris').css('font-weight', 'normal');
    }

    function clickTokyo() {
      // document.getElementById('photo').src = 'images/tokyo.png';
      // jQuery 사용 문법
      $('#photo').attr('src', 'images/tokyo.png');

      $('#home').css('font-weight', 'normal');
      $('#seoul').css('font-weight', 'normal');
      $('#tokyo').css('font-weight', 'bold');
      $('#paris').css('font-weight', 'normal')

    }
    
    function clickParis() {
      // document.getElementById('photo').src = 'images/paris.png';
      // jQuery 사용 문법
      $('#photo').attr('src', 'images/paris.png');

      $('#home').css('font-weight', 'normal');
      $('#seoul').css('font-weight', 'normal');
      $('#tokyo').css('font-weight', 'normal');
      $('#paris').css('font-weight', 'bold');
    }

    // 사진에 마우스 갖다 댔을 때 그림자 생성

    function mouseEnterPhoto() {
      $('#photo').css('box-shadow', '5px 10px');
    }

    // 그림자 제거
    function mouseLeavePhoto() {
      $('#photo').css('box-shadow', 'none');
    }

    // 키보드 이벤트 핸들링
    function processKeyEvent(event) {
      if (event['key'] === '1') {
        clickHome();
      } else if (event['key'] === '2') {
        clickSeoul();
      } else if (event['key'] === '3') {
        clickTokyo();
      } else if (event['key'] === '4') {
        clickParis();
      }
    }



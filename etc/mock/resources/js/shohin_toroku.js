$(function(){
	// wow
	new WOW().init();
	
	// easeScroll
	$("html").easeScroll({
		frameRate: 60,
		animationTime: 1000,
		stepSize: 120,
		pulseAlgorithm: 1,
		pulseScale: 8,
		pulseNormalize: 1,
		accelerationDelta: 20,
		accelerationMax: 1,
		keyboardSupport: true,
		arrowScroll: 50,
		touchpadSupport: true,
		fixedBackground: true
	});

	// 下部ボタンの位置調整
	$(window).scroll(function(e) {
		let circleBtn = $('.circle_btn');
		$window = $(e.currentTarget);
		windowHeight = $window.height(); // ウィンドウの高さ
		pageHeight = $(document).height(); // ページの高さ
		// footerHeight = $('.footer').height(); // フッタの高さ
		footerHeight = 120; // フッタの高さ
		scrollTop = $window.scrollTop(); // スクロールした量
		bottom = windowHeight + scrollTop + footerHeight - pageHeight;

		if (scrollTop >= pageHeight - windowHeight - footerHeight) {
			circleBtn.css("bottom", bottom);
		} else {
			circleBtn.css("bottom", 0);
		}	
	});
	
	// 下部ボタンの初期位置
	$('.circle_btn').css("bottom", 0);
});
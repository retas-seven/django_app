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

	// animsition
	// $(".animsition").animsition();
	$(".animsition").animsition({
		inClass: 'fade-in',
		outClass: 'fade-out-up-sm',
		inDuration: 500,
		outDuration: 500,
		linkElement: '.animsition-link',
		// e.g. linkElement: 'a:not([target="_blank"]):not([href^="#"])'
		loading: true,
		loadingParentElement: 'body', //animsition wrapper element
		loadingClass: 'animsition-loading',
		loadingInner: '', // e.g '<img src="loading.svg" />'
		timeout: false,
		timeoutCountdown: 5000,
		onLoadEvent: true,
		browser: [ 'animation-duration', '-webkit-animation-duration'],
		// "browser" option allows you to disable the "animsition" in case the css property in the array is not supported by your browser.
		// The default setting is to disable the "animsition" in a browser that does not support "animation-duration".
		overlay : false,
		overlayClass : 'animsition-overlay-slide',
		overlayParentElement : 'body',
		// transition: execute(url)
		transition: function(url){
			if (url === void 0 || url == '') {
				return;
			} else {
				window.location.href = url;
			}
		}
	});

	// 登録／更新ボタン押下時の処理
	$(".js_execute_btn").on("click", execute);
});

/**
 * 登録／更新ボタン押下時の処理
 */
function execute() {
	$('body').on('animsition.outEnd', executeMain);
};

function executeMain() {
	window.location.href = 'list.html';
};

$(document).ready(function() {
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
		// transition: function(url){ window.location.href = url; }
		transition: function(url){
			if (url === void 0 || url == '') {
				return;
			} else {
				window.location.href = url;
			}
		}
	});

	// 画面の初期状態を設定
	init();
	// 登録／更新ボタン押下時の処理
	$(".js_execute_btn").on("click", execute);
});

/**
 * 画面初期化
 */
function init() {
	let form = $('[name=shohin_form]');

	if (mode == 'regist') {
		form.attr('action', shohin_regist_view_url);

	} else if (mode == 'update') {
		form.attr('action', shohin_update_view_url);
		// 型番は読み取りのみとし、更新させない
		$('#id_kataban').attr('readonly', true);
		// $('#id_kataban').addClass('form-control-plaintext');
	}
};

/**
 * 登録／更新ボタン押下時の処理
 */
function execute() {
	$('body').on('animsition.outEnd', () => {
		let form = $('[name=shohin_form]');
		form.submit();
	});
};


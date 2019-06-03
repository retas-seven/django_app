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

	// 削除ボタン押下時の処理
	$(".js_delete_btn").on("click", execDelete);

	// 更新ボタン押下時の処理
	$(".js_update_btn").on("click", execUpdate);
});

/**
 * 削除ボタン押下時の処理
 */
function execDelete() {
	if(!confirm('削除しますか？')){
		return false;
	}
	
	nohinId = $(this).parents('td').data('nohin_id');
	form = $('[name=nohin_id_form]');
	form.attr('action', nohinDeleteViewUrl);
	$('.js_nohin_id').val(nohinId);

	$('body').on('animsition.outEnd', () => {
		form.submit();
	});
}

/**
 * 更新ボタン押下時の処理
 */
function execUpdate() {
	nohinId = $(this).parents('td').data('nohin_id');

	$('body').on('animsition.outEnd', () => {
		window.location.href = nohinUpdateViewUrl + '?nohin_id=' + nohinId
	});
}

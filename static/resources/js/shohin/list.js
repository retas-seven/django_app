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

	/**
	 * 削除ボタン押下時の処理
	 */
    $('.js_delete_btn').click(function(e) {
        if(!confirm('削除しますか？')){
            return false;
        }
		
		kataban = $(this).parents('td').data('kataban');
		form = $('[name=shohin_kataban_form]');
		form.attr('action', shohin_delete_view_url);
		$('.js_shohin_kataban').val(kataban);
		form.submit();
	});
	
	/**
	 * 登録ボタン押下時の処理
	 */
    $('.js_regist_btn').click(function(e) {
		
	});
	
	/**
	 * 更新ボタン押下時の処理
	 */
    $('.js_update_btn').click(function(e) {

	});
});
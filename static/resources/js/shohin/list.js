$(function(){
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
	
	kataban = $(this).parents('td').data('kataban');
	form = $('[name=shohin_kataban_form]');
	form.attr('action', shohin_delete_view_url);
	$('.js_shohin_kataban').val(kataban);

	$('body').on('animsition.outEnd', () => {
		form.submit();
	});
}

/**
 * 更新ボタン押下時の処理
 */
function execUpdate() {
	kataban = $(this).parents('td').data('kataban');

	$('body').on('animsition.outEnd', () => {
		window.location.href = shohin_update_view_url + '?kataban=' + kataban
	});
}

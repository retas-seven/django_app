$(document).ready(function() {
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

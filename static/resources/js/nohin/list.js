$(document).ready(function() {
	// 削除ボタン押下時の処理
	$(".js_delete_btn").on("click", execDelete);

	if (mode == 'list') {
		// 更新ボタン押下時の処理
		$(".js_update_btn").on("click", execUpdate);

	} else if (mode == 'pdf_list') {
		// PDFダウンロードボタン押下時の処理
		$(".js_pdf_download_btn").on("click", execPdfDownload);
	}
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

/**
 * PDFダウンロードボタン押下時の処理
 */
function execPdfDownload() {
	// ダウンロード開始時にスピナーを表示して、終了時に非表示にする
	$('#loading').fadeIn();
	$.removeCookie('loading_finish_flg');

	nohinId = $(this).parents('td').data('nohin_id');
	window.location.href = deliveryNoteViewUrl + '?nohin_id=' + nohinId

	// TODO:
	// サーバ側で設定された「loading_finish_flg」が存在することを条件として、スピナーを非表示にしているが、
	// ファイルがダウンロードされるタイミングとスピナーが非表示になるタイミングがズレていて、
    // なぜズレるかが不明。調べる必要あり。
	let checkCookie = () => {
		if ($.cookie('loading_finish_flg') == void 0) {
			setTimeout(checkCookie, 1000);
			// console.log('waiting...');
		} else {
			$('#loading').fadeOut();
			$.removeCookie('loading_finish_flg');
			// console.log('finish!!');
		}
	} 
	setTimeout(checkCookie, 1000);
}
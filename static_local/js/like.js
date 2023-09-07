// like.js
function toggleLike(postId) {
    // Django CSRFトークンを取得
    const csrftoken = getCookie('csrftoken');
    // memevo_app/likepost/
    // Ajaxリクエストを送信
    fetch(`/memevo_app/folderlist/${postId}/likepost/${postId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        credentials: 'same-origin',
    })
        .then(response => response.json())
        .then(data => {
            // いいねの状態を更新
            const likeLink = document.querySelector(`[onclick="toggleLike(${postId})"]`);
            const likeCountSpan = likeLink.querySelector('h4');
            const likeIcon = likeLink.querySelector('svg.like-icon');
            console.log(likeCountSpan.textContent)
            likeCountSpan.textContent = data.like_count;

            // いいねの状態に応じてsvg要素のクラスを切り替え
            if (data.is_liked) {
                likeIcon.classList.remove('not-liked');
                likeIcon.classList.add('liked');
            } else {
                likeIcon.classList.remove('liked');
                likeIcon.classList.add('not-liked');
            }

            // data.like_count;
            // likeLink.innerText = data.is_liked ? 'いいね解除' : 'いいね';
        })
        .catch(error => console.error('Error:', error));
}


// DOMがロードされた後に実行する処理
document.addEventListener('DOMContentLoaded', function () {
    // すべてのいいねボタンのクリックイベントを設定
    const likeLinks = document.querySelectorAll('[onclick^="toggleLike"]');
    likeLinks.forEach(likeLink => {
        likeLink.addEventListener('click', function () {
            const postId = parseInt(likeLink.getAttribute('onclick').match(/\d+/)[0]);
            toggleLike(postId);
        });
    });
});

// CSRFトークンを取得するヘルパー関数
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
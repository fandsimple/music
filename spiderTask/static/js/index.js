window.onload = function () {
    var box = document.getElementById("box");
    var audioVice = document.getElementById("vice");
    audioVice.volume = 0.4;
    //歌曲标识
    count = 1;
    //歌曲总数
    var allMusicNum = 7;

    //播放和暂停
    var playBut = document.getElementById("play");
    var pauseBut = document.getElementById("pause");
    playBut.addEventListener("click", function () {
        audioVice.play();
        playBut.style.display = 'none';
        pauseBut.style.display = "block";
    }, false);
    pauseBut.addEventListener("click", function () {
        audioVice.pause();
        pauseBut.style.display = "none";
        playBut.style.display = "block";
    }, false);

    //上一曲下一曲
    var beforeBut = document.getElementById("before");
    var afterBut = document.getElementById("after");
    beforeBut.addEventListener("click", function () {
        count--;
        if (count <= 0) {
            //重头循环
            count = allMusicNum;
        }
        audioVice.src = "http://127.0.0.1:8000/static/music/5.mp3";
        // console.log(audioVice.src);
        audioVice.play();
        pauseBut.style.display = "block";
        playBut.style.display = "none";
    }, false);

    afterBut.addEventListener("click", next, false);

    function next() {
        count++;
        if (count > allMusicNum) {
            //重头循环
            count = 1;
        }
        audioVice.src = "https://m7.music.126.net/20200207000621/d5875e00ce58c36308136dc195bb7723/ymusic/8972/6e6e/7b86/bddf788bf92e62d7c5c9aa457dd27bf5.mp3";
        // console.log(audioVice.src);
        audioVice.play();
        pauseBut.style.display = "block";
        playBut.style.display = "none";
    }

    //播放模式的实现
    var loopObj = document.getElementById("loop");
    var orderObj = document.getElementById("order");
    //循环模式
    loopObj.addEventListener("click", function () {
        loopObj.style.display = "none";
        orderObj.style.display = "block";
        audioVice.loop = "";
        timer = setInterval(isEnd, 1000);
    }, false);

    //顺序模式
    orderObj.addEventListener("click", function () {
        orderObj.style.display = "none";
        loopObj.style.display = "block";
        audioVice.loop = "loop";
        clearInterval(timer);
    }, false);


    //检测是否歌唱完毕
    var timer = setInterval(isEnd, 1000);

    function isEnd() {
        if (audioVice.currentTime == audioVice.duration) {
            next();
        }
    }

    //实现音量的调节
    var vLenghtObj = document.getElementById("vLength");
    var vLength1Obj = document.getElementById("vLengh1");
    var vcObj = document.getElementById("vC");
    var min = vcObj.offsetLeft;
    var max = vcObj.offsetLeft + 200;
    vcObj.addEventListener("mousedown", function (e) {
        var baseX = e.pageX;
        box.addEventListener("mouseover", mover, false);

        function mover(e) {
            //计算偏移量
            var moveX = 0;
            moveX = e.pageX - baseX;
            baseX = e.pageX;
            local = vcObj.offsetLeft + moveX;
            //桌面样式的改变
            if (local > max) {
                //小球超出设置
                vcObj.style.left = max + "px";
            } else if (local < min) {
                vcObj.style.left = min + "px";
            }
            vcObj.style.left = local + "px";
            vLength1Obj.style.width = moveX + parseInt(window.getComputedStyle(vLength1Obj, null).width) + "px";

            //音量值的设定
            volumeNum = moveX / 200;
            audioVice.volume = audioVice.volume + volumeNum;
            // console.log(audioVice.volume);

        }

        vcObj.addEventListener("mouseup", function () {
            box.removeEventListener("mouseover", mover, false);
        }, false);
        box.addEventListener("mouseup", function () {
            box.removeEventListener("mouseover", mover, false);
        }, false);
    }, false);

    //静音
    var volumeBut = document.getElementById("volume");
    var muteBut = document.getElementById("mute");
    volumeBut.addEventListener("click", function () {
        volumeBut.style.display = "none";
        muteBut.style.display = "block";
        audioVice.volume = 0;
        vcObj.style.left = "710px";
        vLength1Obj.style.width = "0px";
    }, false);

    //取消静音
    muteBut.addEventListener("click", function () {
        volumeBut.style.display = "block";
        muteBut.style.display = "none";
        audioVice.volume = 0.4;
        vcObj.style.left = "790px";
        vLength1Obj.style.width = "80px";
    }, false);

    //	实现播放进度
    var dLengthObj = document.getElementById("dLength");
    var dLength1Obj = document.getElementById("dLength1");
    var dcObj = document.getElementById("dC");
    var planTimer = setInterval(function () {
        var movePiex = audioVice.currentTime / audioVice.duration * 600;
        dLength1Obj.style.width = movePiex + "px";
//		dcObj.style.left = (window.getComputedStyle(dcObj,null).left)
        dcObj.style.left = 300 + movePiex + "px";

    }, 10);

    //设置播放时间
    var currentObj = document.getElementById("currentTime");
    var endObj = document.getElementById("endTime");
    var currentTime = setInterval(function () {
        var endtime = audioVice.duration;
        var currenttime = audioVice.currentTime;
        currenttime = calculateTime(currenttime);
        endtime = calculateTime(endtime);
        currentObj.innerHTML = currenttime;
        endObj.innerHTML = endtime;
    }, 100);

    //计算时间函数封装
    function calculateTime(second) {
        var tt = (parseFloat(second / 60).toFixed(2)).toString();
        var tInt = tt.split(".")[0];
        var tFloat = parseInt(parseFloat("0." + tt.split(".")[1]) * 60);
        var timeStr = tInt + ":" + tFloat;
        // console.log(timeStr);
        return timeStr;

    }


    function getSongByListTag() {
        $.post("/spidertask/getSongListById", {playlistTag: '华语'}, function (result) {
            var songList = result.playlist.tracks;
            var playlistTag = result.mytag;
            // console.log(songList);
            var $ul = $("#songList");
            var tag = $("<li id='tag' data='" + playlistTag + "' style='margin-bottom: 10px;'>类别：" + playlistTag + "</li>");
            $ul.append(tag);
            for (var i = 0; i < songList.length; i++) {
                var $li = $("<li songId='" + songList[i].id + "' onclick='getSong(this)'>" + songList[i].name.substring(0, 30) + "</li>");
                $ul.append($li);
            }
        });
    }

    getSongByListTag(); // 初始化歌单列表

    // 为换一批按钮添加事件
    var change = document.getElementById("change");
    change.addEventListener("click", function () {
        var tag = $('#tag').attr('data');
        $.post("/spidertask/getSongListById", {playlistTag: tag}, function (result) {
            var songList = result.playlist.tracks;
            var playlistTag = result.mytag;
            // console.log(songList);
            var $ul = $("#songList");
            $ul.empty();
            var tag = $("<li id='tag' data='" + playlistTag + "' style='margin-bottom: 10px;'>类别：" + playlistTag + "</li>");
            $ul.append(tag);
            for (var i = 0; i < songList.length; i++) {
                var $li = $("<li songId='" + songList[i].id + "'>" + songList[i].name.substring(0, 30) + "</li>");
                $ul.append($li);
            }
        });
    }, false);


    function getSong(obj) {
        var songId = obj.songId; //曲Id
        var songName = obj.text; //曲名
        var tag = $('#tag').attr('data'); // 歌曲分类
        var userId = $('#user span').attr('userId'); // 用户Id

        //请求网易云音乐接口
        $.get(
            "https://api.imjad.cn/cloudmusic/?type=song&id=28012031&br=128000", {}, function (data, state) {
                //这里显示从服务器返回的数据
                alert(data);
            }
        );

        // 请求自己后台，记录用户听过歌曲
        $.get(
            "/spidertask/", {
                songId: songId,
                songName: songName,
                songTag: tag,
                userId: userId,
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log('记录成功');
            }
        );
    }


    // 为搜索按钮添加点击事件
    var serachBtn = document.getElementById("search_button");
    serachBtn.addEventListener('click', function () {
        var searchContent = $('#appendedInputButton')[0].value;
        $.get(
            "https://api.imjad.cn/cloudmusic/", {
                type: 'search',
                search_type: 1,
                s: searchContent,
            }, function (data, state) {
                //这里显示从服务器返回的数据
                console.log(data);
                var songs = data.result.songs;
                var $ul = $("#sameList");
                $ul.empty();
                for (var i = 0; i < 8; i++) {
                    var $li = $("<li songId='" + songs[i].id + "' onclick='getSong(this)'>" + songs[i].name.substring(0,13) + "</li>");
                    $ul.append($li);
                }
            }
        );
    });


}
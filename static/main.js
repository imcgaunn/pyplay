LAMBDA_ENDPOINT = 'https://noi5erl8ie.execute-api.us-east-1.amazonaws.com/dev/podcast/';

// prompt should be displayed on line after last podcast
// feed.

// view for each feed should show 5 most recent feed entries
// and allow user to scroll through list.


function get_session_token() {
    // TODO:
    // first try to get token from localstorage

    // if not there, create a new one and save it
    // in localstorage.
    // called by get init state during application startup
}

function get_init_state() {
    // TODO:
    // ask backend to fetch state for token, or send back a default
    // called at application startup
}

function update_state(s) {
    // TODO:
    // send current state to backend.
}

function toggle_player(ev) {
    // TODO:
    // stops/starts selected audio file. triggered by keyboard event
}

function seek(ev) {
    // TODO:
    // seeks active player. triggered by keyboard event
}

function add_subscription(feed_url) {
    // a 'subscription' as far as pyplay is concerned is just another
    // view in the list of views.
    var insert_pos = $('#feedinput').before()
}

function remove_subscription(feed_url) {

}

function get_feed_info(feed_url) {
    // should call lambda function behind API gateway.

    var success_func = function (data, res, xhr) {
        build_podcast_view(data);
    }

    var payload = JSON.stringify({'url': feed_url});
    $.post(LAMBDA_ENDPOINT + "info",
        payload,
        success_func);
}

function build_entry_view(entry_info) {
    var parent = $('<div>', {'class': 'entryview'})
    var title = $('<h4>', {'text': entry_info['title']});
    var playbutton = $('<button>', {
        'class': 'play',
        'text': 'play'
    });
    var stopbutton = $('<button>', {
        'class': 'stop',
        'text': 'stop'
    });
    var audio_link = entry_info['links'][0]['href'];
    var player = $('<audio>', {'src': audio_link});
    playbutton.click(function () {
        // create audio elem and start playing
        parent.append(player);
    });
    stopbutton.click(function () {
        // delete audio elem. we don't want to keep
        // too many audio players around.
        player.delete();
    });
    parent.append(title);
    parent.append(playbutton);
    return parent;
}

function build_podcast_view(podcast_info) {
    var parent = $('<div>', {'class': 'podcastview'});

    var title = podcast_info['title'];
    var artwork = podcast_info['artwork'];
    var entries = podcast_info['entries'];

    for (var i in entries) {
        var res = build_entry_view(entries[i]);
        parent.append(res);
    }
    $("#feedinput").before(parent);
}

// attach events
$('#feedinput input').bind('keypress', function (e) {
    var code = e.which;
    if (code == 13) {
        var url = $('#feedinput input').val()
        var info = get_feed_info(url);
        // scroll to pos of prompt
        var prompt_top = $('#feedinput').offset().top;
        $('html, body').animate({scrollTop: prompt_top});
    }
});

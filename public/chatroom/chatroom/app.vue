<style>

h4,
h3 {
    display: inline
}

.wrapper_fix {
    background-color: palegoldenrod!important;
}

.button_fix {
    width: 5%!important;
}

.message-block {
    margin-top: 5px;
    width: 100%;
}

.message-text_left {
    float: left
}

.message_text_right {
    display: block;
    text-align: right;
}

.message_panel {
    width: 70%;
}

.chat-panel {
    height: 403px;
    overflow-y: auto
}

.user-panel {
    height: 175px;
    overflow-y: auto
}

.room-panel {
    height: 175px;
    overflow-y: auto
}

.padding-fix {
    padding-left: 85px !important;
    padding-right: 30px !important
}

.padding_horizotal_fix {
    padding-left: 5px !important;
    padding-right: 10px !important
}

.padding_vertical_fix {
    padding-top: 5px !important;
    padding-bottom: 5px !important
}

.custom-active {
    background: #428bca;
    border-radius: 8px;
    color: white
}

.custom-active a {
    color: white
}

.custom-active a:hover {
    color: white
}

#room-list a {
    text-decoration: none
}

.room-text {
    margin-left: -7px !important;
    margin-top: 0px !important;
    padding: 3px 6px 3px 7px !important
}

.room-text label {
    margin: 0px !important
}

.container_padding {
    padding-top: 20px;
}

.div_center {
    margin: 0 auto;
}

.history_hr {
    height: 1px;
    border: none;
    border-top: 1px solid #555555;
    margin-bottom: 6px;
    margin-top: 0px;
}

.room-text:hover {
    background: #E8E8E8;
    border-radius: 8px
}

.custom-active:hover {
    background: #428bca;
    border-radius: 8px
}

.menu-image {
    float: left;
    margin-bottom: -90px
}

.border-form-div {
    max-width: 400px;
    padding: 5px 29px 29px;
    margin: 0 auto 20px;
    background-color: #fff;
    border: 1px solid #e5e5e5;
    -webkit-border-radius: 5px;
    -moz-border-radius: 5px;
    border-radius: 5px;
    -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05)
}

.border-form-div h2 {
    margin-bottom: 20px
}

.form-inputs .checkbox {
    margin-left: 20px
}

.alert-error {
    padding: 0px !important
}

.form-control {
    border: 1px solid #428bca !important
}

.panel.panel-primary {
    margin-bottom: 10px !important
}

.message_history {
    font-size: 10px;
    color: #424242;
    text-align: center;
    padding-bottom: 8px;
    width: 90%;
    float: left;
    padding-left: 10%;
}

.navbar-brand {
    font-size: 22px !important;
    color: #444 !important
}

.navbar-link {
    color: #444 !important
}

i {
    width: 14px;
    text-align: center
}

.panel {
    background-color: #f8f8f8 !important
}

.navbar-default {
    background-color: #F0F0F0 !important;
    border-color: #D8D8D8 !important
}

.user-image {
    vertical-align: text-top
}

p {
    margin-bottom: 0px !important
}

body {
    background-color: #CCC !important
}

.git label {
    margin-bottom: -10px
}

.git {
    padding-bottom: 7px !important;
    border: 1px solid !important;
    border-color: #428bca !important
}

.created {
    float: left
}

.credit {
    display: block;
    text-align: center;
    margin: 0 auto
}

.alert_float {
    position: fixed;
    z-index: 100;
    width: 100%;
    line-height: 40%;
    padding-bottom: 5px;
    padding-top: 15px;
}

#user_option {
    width: 120px!important;
}

.input_label {
    line-height: 35px;
}

#connect-form {
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
    width: 340px;
    box-shadow: #aaa 0px 0px 12px 2px;
    border-radius: 5px 5px 5px 5px;
}

#login_head {
    margin-top: 90px;
    margin-left: auto;
    margin-right: auto;
    font-size: 24px!important;
}

</style>

<template>

<div class="wrapper wrapper_fix">

    <nav class="navbar navbar-default" role="navigation" v-if="user_status">
        <div class="container">
            <div class="navbar-header">
                <a href="https://github.com/Maimer/chatter"><img alt="Chatter" class="menu-image" height="65" src="./assets/img/logo.png" width="65"></a>
                <a class="navbar-brand padding-fix" href="https://github.com/Maimer/chatter">Chat Room</a>
            </div>
            <div>
                <p class="navbar-text navbar-right padding-fix">
                    <a class="navbar-link" href="http://sockets-chat.herokuapp.com/users/edit">{{ nick_name }}</a> |
                    <a class="navbar-link" data-method="delete" href="#" rel="nofollow" @click="sign_out">Sign Out</a>
                </p>
            </div>
        </div>
    </nav>
    <div class="alert alert-danger alert_float" role="alert" v-if=alert>
        <p class="text-center">
            {{alert}}
        </p>
    </div>

    <div class="container container_padding" v-if="user_status">
        <div class="row">
            <div class="col-md-9">
                <chat_log :message_pkg='message_pkg' :room_name='room_name' :message_pkg_history='message_pkg_history'></chat_log>

                <input_section :user_list="user_list"></input_section>
            </div>
            <div class="col-md-3">
                <user_list :user_list="user_list"></user_list>
            </div>
        </div>
        <br>
    </div>


    <p class="text-center" id="login_head" v-if="!user_status">
        Chat Room
    </p>
    <div id="connect-form" v-if="!uid">

        <form class="form-horizontal well">
            <div class="form-group">
                <label for="input_pnum" class="col-md-3 control-label">Phone Number</label>
                <div class="col-md-8">
                    <input type="text" class="form-control" id="input_pnum" placeholder="Phone Number" v-model="pnum">
                </div>
            </div>
            <div class="form-group">
                <label for="input_password" class="col-md-3 control-label">Password</label>
                <div class="col-md-8">
                    <input type="password" class="form-control" id="input_password" placeholder="Password" v-model="password">
                </div>
            </div>
            <div class="form-group">
                <div class="intput-group">
                    <button type="button" class="btn btn-default" @click="login">Sign in</button>
                    <button type="button" class="btn btn-default pull-right" @click="sign_up">Sign up</button>
                </div>

            </div>
        </form>

    </div>

    <div id="connect-form" v-if="uid && !user_status">
        <form name="connect" class="well form-horizontal">
            <div class="form-group">
                <label for="Nickname" class="col-md-5 control-label">Nick Name</label>
                <div class="col-md-6">
                    <input type="text" placeholder="Nickname" class="form-control" v-model="nick_name">
                </div>
            </div>
            <button type="button" id="connect-button" class="btn btn-primary btn-lg btn-block" @click="register">Done</button>
        </form>
    </div>

</div>

</template>

<script>

var chat_log = require('./component/chat_log.vue');
var user_list = require('./component/user_list.vue');
var input_section = require('./component/input_section.vue');

export default {
    data() {
            return {
                message_pkg: [],
                message_pkg_history: [],
                user: {},
                nick_name: '',
                uid: '',
                user_list: [],
                room_name: 'Chat Room',
                alert: '',
                user_status: '',
            }
        },
        components: {
            chat_log: chat_log,
            user_list: user_list,
            input_section: input_section,
        },

        methods: {
            login: function() {
                var that = this;
                var paramData = {};

                paramData['pnum'] = this.pnum;
                paramData['password'] = this.password;

                this.$http.get('/login.do?' + json2url(paramData)).then(function(response) {
                    var data = response.data;
                    if (!data)
                        return
                        // data.forEach(function(item) {});
                    if (data.data && data.data.uid) {
                        console.log(data)
                        this.uid = data.data.uid;
                        this.user_name = data.data.user_name;
                        this.user["nick_name"] = data.data.user_name;
                        this.user['password'] = data.data['password'];
                        this.user["uid"] = this.uid;
                        this.user_status = data.data.status;
                        wsCache.set("user", this.user);
                        ws_init(that); //  初始化ws
                    } else if (data.data) {
                        this.alert = data.data
                    }
                })
            },
            sign_up: function() {
                var that = this;
                var paramData = {};
                var uid = parseInt(Math.random() * 100000000);

                paramData['pnum'] = this.pnum;
                paramData['password'] = this.password;
                this.$http.get('/login.do?' + json2url(paramData)).then(function(response) {
                    var data = response.data;
                    if (!data)
                        return
                        // data.forEach(function(item) {});
                    if (data.code == 1 || data.code == 0) {
                        this.alert = "This phone number has been registered"
                    } else {
                        this.uid = uid;
                    }
                })
            },
            register: function() {
                var that = this;
                var paramData = {};
                paramData['pnum'] = this.pnum;
                paramData['password'] = this.password;
                paramData['user_name'] = this.nick_name;
                paramData['uid'] = this.uid;

                this.$http.post('/register.do', paramData).then(function(response) {
                    var data = response.data;
                    if (!data)
                        return
                    if (data.code == 0) {
                        this.uid = data.data['uid'];
                        this.user_name = data.data['user_name'];
                        this.user['password'] = data.data['password'];
                        this.user["nick_name"] = this.nick_name;
                        this.user["uid"] = this.uid;
                        this.user_status = data.data.status;
                        wsCache.set("user", this.user);
                        ws_init(that); //  初始化ws
                    }
                });

            },
            print_response: function(jsondata) {
                if (jsondata["TYPE"] == MESSAGE) {
                    this.message_pkg.push({
                        'time': jsondata['TIME'].substr(5, 11),

                        "message_type": MESSAGE,
                        "from": jsondata["SENDER"].user_name,
                        "from_uid": jsondata["SENDER"].uid,
                        "message_body": jsondata["MESSAGE"]
                    })

                } else if (jsondata["TYPE"] == PRIVATE_MESSAGE) {
                    this.message_pkg.push({
                        'time': jsondata['TIME'].substr(5, 11),

                        "message_type": PRIVATE_MESSAGE,
                        "from": jsondata["SENDER"].user_name + " (private)",
                        "from_uid": jsondata["SENDER"].uid,
                        "message_body": jsondata["MESSAGE"]
                    })

                } else if (jsondata["TYPE"] == JOIN) {
                    this.message_pkg.push({
                        'time': jsondata['TIME'].substr(5, 11),
                        "from": "server",
                        "message_body": jsondata["USER_NAME"] + " joined, welcome!!"
                    })

                } else if (jsondata["TYPE"] == NAMECHANGE) {
                    return
                } else if (jsondata["TYPE"] == LEAVE) {
                    this.message_pkg.push({
                        'time': jsondata['TIME'].substr(5, 11),
                        "from": 'server',
                        "message_body": jsondata['USER'] + "las left!"
                    })
                } else if (jsondata["TYPE"] == USERLIST) {
                    this.user_list = jsondata['USERS'];
                } else if (jsondata["TYPE"] == ERROR) {
                    return
                }
            },
            sign_out: function() {
                wsCache.clear();
                ws.close();
                this.uid = '';
                this.user_status = '';

            },
            get_message_history: function(index) {

                var paramData = {};
                paramData['uid'] = this.user['uid'];
                paramData['password'] = this.user['password'];
                paramData['last_msg_id'] = index;

                this.$http.get('/message_history.do?' + json2url(paramData)).then(function(response) {
                    var data = response.data;
                    if (!data)
                        return
                    if (data.code == 1) {
                        this.alert = data.data;
                    } else {
                        data.data.forEach(function(item) {
                            this.message_pkg_history.push({
                                'time': item.time.substr(5, 11),
                                "from": item.from,
                                "message_type": item.message_type,
                                "from_uid": item.from_uid,
                                "message_body": item.message_body,
                            })
                        }.bind(this));

                    }
                })
            }
        },
        events: {
            'send_message': function(message) {
                ws.send(create_msg_pkg(message))
            },
            'send_private_message': function(data) {
                if (this.uid == data.to) {
                    alert("No need to send message to myself");
                    return
                }
                ws.send(create_private_msg_pkg(data.to, data.message))
            },
            'alert': function(info) {
                this.alert = info;
            }
        },
        watch: {
            'alert': function(a, b) {
                var that = this;
                setTimeout(function() {
                    that.alert = '';
                }, 3000);
            }
        },
        ready() {
            var that = this;
            var user = wsCache.get("user");
            if (user && user.uid && user.nick_name) {

                this.nick_name = user.nick_name;
                this.uid = user.uid;
                this.user_status = 1;
                this.user = user;
                ws_init(that)
                this.get_message_history(-1); // get 10 latest message from data table
            }
        },
}

// Different message types
var MESSAGE = 0;
var PRIVATE_MESSAGE = 1;

var NAMECHANGE = 11;
var JOIN = 12;
var LEAVE = 13;
var USERLIST = 14;
var ERROR = 15;

function ws_init(that) {

    var ws = new WebSocket("ws://localhost:8888/chat");
    window.ws = ws;

    ws.onopen = function() {
        ws.send(create_join_pkg(that.nick_name, that.uid));
    }
    ws.onmessage = function(event) {
        var jsondata = jQuery.parseJSON(event.data);
        that.print_response(jsondata)
    }
    ws.onclose = function() {
        console.log("websocket closed");
    }
}

function create_msg_pkg(message) {
    var msg = {
        "TYPE": MESSAGE,
        "MESSAGE": message
    };
    return JSON.stringify(msg);
}

function create_private_msg_pkg(to, message) {
    var msg = {
        "TYPE": PRIVATE_MESSAGE,
        "TO": to,
        "MESSAGE": message
    };
    return JSON.stringify(msg);
}

function create_userlist_pkg() {
    var msg = {
        "TYPE": USERLIST
    };
    return JSON.stringify(msg);
}

function create_join_pkg(name, uid) {
    var msg = {
        "TYPE": JOIN,
        "USER_NAME": name,
        "UID": uid
    };

    return JSON.stringify(msg);
}

</script>

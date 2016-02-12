

<template>

<div class="panel panel-primary">
    <div class="panel-heading">
        <h3 class="panel-title" id="chatbox-header">{{ room_name }}</h3>
    </div>
    <div id="chat2" class="panel-body chat-panel">
        <div class="tab-content">
            <div class="tab-pane active">
                <!-- <div class="message-block" v-for="item in message_pkg"> -->

                <div class="panel panel-default message_panel" v-for="item in message_pkg_history" v-bind:class="{ 'pull-right' : item.from_uid == uid , 'pull-left' : item.from_uid != uid }">
                    <div class="message_text_right" v-bind:class="{message_text_right : item.from_uid == uid}">
                        <span class="label label-info">[{{ item.time }}]<span v-if=" item.from_uid != uid ">{{ item.from }}:</span><span v-if=" item.message_type == 1 ">{{ private }}:</span></span>
                    </div>

                    <div class="panel-body">
                        {{ item.message_body }}
                    </div>
                </div>
                <div class="message_history">
                    <span>history</span>
                    <hr width="100%" class="history_hr">
                </div>
                <div class="panel panel-default message_panel" v-for="item in message_pkg" v-bind:class="{ 'pull-right' : item.from_uid == uid , 'pull-left' : item.from_uid != uid }">
                    <div class="message_text_right" v-bind:class="{message_text_right : item.from_uid == uid}">
                        <span class="label label-info">[{{ item.time }}]<span v-if=" item.from_uid != uid ">{{ item.from }}:</span><span v-if=" item.message_type == 1 ">{{ private }}:</span></span>
                    </div>

                    <div class="panel-body">
                        {{ item.message_body }}
                    </div>
                </div>

                <!-- </div> -->
            </div>
        </div>
    </div>

</template>

<script>

export default {
    data() {
            return {
                uid: '',
            }
        },
        props: ['message_pkg', 'message_pkg_history', 'room_name'],
        methods: {

        },
        watch: {
            "message_pkg": function(val, oldVal) {
                this.$nextTick(function() {
                    var div = document.getElementById("chat2");
                    div.scrollTop = div.scrollHeight;
                })
            },
        },
        ready: function() {
            var user = wsCache.get("user");
            if (user && user.uid && user.nick_name) {
                this.uid = user.uid;
            }
        }

}

</script>

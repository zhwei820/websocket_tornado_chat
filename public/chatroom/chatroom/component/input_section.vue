

<template>

<div class="wrapper">
    <form id="input-message" class="form-inline padding_vertical_fix">
        <div class="form-group col-md-3">
            <label for="message" class="input_label">To all</label>
        </div>
        <div class="input-group col-md-9">
            <input type="text" id="message" class="form-control" placeholder="Message..." autofocus="" v-model="message_body">
            <span class="input-group-btn button_fix">
                    <button id="send" class="btn btn-primary" @click="send_message_click">Send!</button>
                </span>
        </div>
    </form>
    <form id="input-message" class="form-inline padding_vertical_fix">
        <div class="form-group col-md-3">
            <label for="message">To</label>
            <select class="form-control" name="" id="user_option" v-model="to_user">
                <option v-for="item in user_list" v-bind:value="item.uid" v-if="uid!=item.uid" selected="selected">{{ item.name }}</option>
            </select>
        </div>

        <div class="input-group col-md-9">
            <input type="text" id="message" class="form-control" placeholder="Message..." autofocus="" v-model="private_message_body" class="col-md-5">
            <span class="input-group-btn button_fix">
                <button id="send" class="btn btn-primary" @click="send_private_message_click">Send!</button>
            </span>
        </div>
    </form>
</div>

</template>

<script>

export default {
    data() {
            return {
                uid: '',
                to_user: '',
            }
        },
        props: ['user_list'],
        methods: {
            send_private_message_click: function() {
                if (this.private_message_body) {
                    this.$dispatch('send_private_message', {
                        to: this.to_user,
                        message: this.private_message_body
                    });
                } else {
                    this.$dispatch("alert", "Please do not send empty message!");
                }
            },
            send_message_click: function() {
                if (this.message_body) {
                    this.$dispatch('send_message', this.message_body)
                } else {
                    this.$dispatch("alert", "Please do not send empty message!");
                }
            }

        },
        ready: function() {
            var user = wsCache.get("user");
            if (user && user.uid && user.nick_name) {
                this.uid = user.uid;
            }
        },
        watch: {
            'user_list': function(val, oldVal) {
                var i = 0
                for (; i < this.user_list.length; i++) {
                    if (this.user_list[i].uid != this.uid) {
                        this.to_user = this.user_list[i].uid;
                        break;
                    }
                }
            },
        }

}

</script>



<template>

<div class="panel panel-primary">


    <div class="panel-heading">
        <h3 id="user-heading" class="panel-title">chat room</h3>
    </div>
    <div class="panel-body user-panel">
        <div id="user-list">

            <div class="user-text" v-for='item in user_list'>
                <i class="glyphicon glyphicon-user"></i>&nbsp;
                <a tabindex="0" role="button" data-toggle="popover" data-trigger="focus" title="uid: {{ item.uid }}" data-content="pnum: {{ item.pnum }}" >{{ item.name }}</a>
            </div>
        </div>
    </div>
</div>

</template>

<script>

export default {
    data() {
            return {
                code: '',
            }
        },
        props: ['user_list'],
        methods: {

        },
        ready: function() {
          setTimeout(function(){
              $('[data-toggle="popover"]').popover();
          }, 200);
        }
}


</script>

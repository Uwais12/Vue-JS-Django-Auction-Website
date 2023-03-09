<template>
    <div class="border rounded bg-secondary shadow p-4 mb-4" :id="'replyForm' + messageId">
        <p class="h1 mb-4">Send a Reply</p>
        <form :id="'newReplyForm' + messageId" @submit.prevent method="POST">
            <div class="form-group">
                <input class="form-control" type="text" name="text" id="text" placeholder="Enter comment" /><br>
                <input style="display:none" class="form-control" name="messageId" id="messageId" :placeholder=messageId
                    :value="messageId" /><br>

                <div class="row justify-content-center">
                    <button v-on:click="send_reply()" class="btn btn-light justify-content-center"
                        type="button">Reply</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

type Response = {
    id: number;
    text: string;
}

export default defineComponent({
    props: ["messageId"],


    data() {

        return {
            responses: [] as Response[],
        };
    },

    methods: {

        async send_reply() {
            let replyForm = document.getElementById('newReplyForm' + this.messageId) as HTMLFormElement;
            let formData: FormData = new FormData(replyForm)
            let val = document.getElementById('messageId') as HTMLFormElement;
            let form1 = document.getElementById('replyForm' + this.messageId) as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }

            let response = await fetch("http://localhost:8000/api/responses", {
                method: "POST",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",

                body: formData
            });
            let data = await response.json();
            this.$emit('changeResponses', data.responses)

        },
    }
})
</script>
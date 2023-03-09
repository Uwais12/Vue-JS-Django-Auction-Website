<template>
    <div style="display: none;" class="border rounded bg-secondary shadow p-4 mb-4" :id="'bidForm' + pid">
        <p class="h1 mb-4">Bid for item</p>
        <form :id="'newBid' + pid" @submit.prevent method="POST">
            <div class="form-group">
                <input class="form-control" type="number" name="bid" :id="'bid' + pid" placeholder="Enter amount"
                    :value=price /><br>

                <input style="display:none" class="form-control" type="number" name="pid" id="pid" placeholder="pid"
                    :value=pid disabled /><br>

                <div class="row justify-content-center">
                    <button @click="send_bid()" class="btn btn-primary btn-lg d-flex justify-content-center mt-3"
                        type="submit">Bid</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';


export default defineComponent({
    props: ["price", "pid"],


    data() {

        return {
            // product: this.starting_price,
        };
    },

    methods: {

        async send_bid() {
            let newBidForm = document.getElementById('newBid' + this.pid) as HTMLFormElement;
            let formData: FormData = new FormData(newBidForm)
            let bidVal = document.getElementById('bid' + this.pid) as HTMLFormElement;
            bidVal = bidVal.value;
            if (bidVal > this.price) {



                let response = await fetch("http://localhost:8000/api/products/" + this.pid, {
                    method: "PUT",
                    body: formData,
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                });
                let data = await response.json();
                this.$emit('changeProducts', data.products)
            }
            else {
                alert('please bid higher than the lowest bid')
            }
        },
    }
})
</script>
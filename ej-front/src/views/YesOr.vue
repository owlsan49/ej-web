<script setup lang="ts">
import { PlusOne } from '@/apis/read.ts'

function pulsOne() {
    console.log('We plus ONE, again!!!!!!!!!!')
    PlusOne({})
        .then(respose => {
            console.log('successfully submit')
        })
        .catch(error => {
            console.log('error')
        })
}
</script>

<template>
    <el-button type="success" round @click="pulsOne" size="large">+ 1</el-button>
</template>

<style scoped></style>
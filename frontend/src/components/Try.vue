<template>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px">Aside</el-aside>
        <el-main>Main</el-main>
        <div>
          Hello World
        </div>
        
        <el-input v-model="input" style="width: 240px" placeholder="Please input" />

        <div class="mb-4">
          <el-button round @click="addUser">Register</el-button>
        </div>
      </el-container>
    </el-container>
  </div>
</template>
  



<script lang="ts">
import axios from 'axios';

export default {
  name: "Try",
  data() {
    return {
      input: '', // 绑定输入框的值
    };
  },
  methods: {
    async addUser() {
      if (!this.input.trim()) {
        this.$message.error('Please enter a valid username.');
        return;
      }
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/add_user', {
          params: {
            username: this.input,
            gender: 'M', // 默认性别，后续可通过选择框调整
          },
        });
        if (response.data.respCode === '000000') {
          this.$message.success('User registered successfully!');
        } else {
          this.$message.error('Registration failed: ' + response.data.respMsg);
        }
      } catch (error) {
        if (error.response) {
          // 服务器响应了错误状态码
          console.error('Response error:', error.response.data);
          console.error('Status code:', error.response.status);
        } else if (error.request) {
          // 请求已发送但没有响应
          console.error('Request error:', error.request);
        } else {
          // 其他类型的错误
          console.error('Other error:', error.message);
        }
        this.$message.error('An error occurred during registration.');
      }
    },
  },
};

import {
  Check,
  Delete,
  Edit,
  Message,
  Search,
  Star,
} from '@element-plus/icons-vue'
import { ref } from 'vue'
const input = ref('')
</script>

<style scoped>
div {
  font-size: 20px;
  color: #000000;
}
</style>

  
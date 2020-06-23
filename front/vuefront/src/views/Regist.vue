<template>
	<div class="regist">
		<strong><van-form @submit="regist">
		  <van-field
		    v-model="username"
		    name="用户名"
		    label="用户名"
		    placeholder="用户名"
		    :rules="[{ required: true, message: '请填写用户名' }]"
		  />
		  <van-field
		    v-model="password"
		    type="password"
		    name="密码"
		    label="密码"
		    placeholder="密码"
		    :rules="[{ required: true, message: '请填写密码' }]"
		  />
		  <van-field
		    v-model="password2"
		    type="password"
		    name="重复密码"
		    label="重复密码"
		    placeholder="重复密码"
		    :rules="[{ required: true, message: '请填写重复密码' }]"
		  />
		  
		  <div style="margin: 16px;">
		    <van-button round block type="info" native-type="submit">
		      提交
		    </van-button>
			<van-field
			  v-model="telephone"
			  type="tel"
			  name="手机号"
			  label="手机号"
			  placeholder="请填写手机号"
			  :rules="[{ required: true, message: '请填写手机号' }]"
			/>
			
			<van-field
			  v-model="sms"
			  center
			  clearable
			  label="短信验证码"
			  placeholder="请输入短信验证码"
			>
			  <template #button>
			    <van-button size="small" type="primary" @click="verfiy">发送验证码</van-button>
			  </template>
			</van-field>	
		  </div>
		</van-form></strong>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				username:"",
				password:"",
				password2:"",
				telephone:"",
				sms:""
			}
		},
		methods:{
			regist(){
				this.$api.regist({
					username:this.username,
					password:this.password,
					password2:this.password2
				}).then(res=>{
					this.$router.push("/login/");
					console.log("请求注册接口",res);
				}).catch(err=>{
					this.$toast("注册失败")
				})
			},
			verfiy(){
				console.log("发送验证码");
				this.$api.sendmsg({
					telephone:this.telephone
				}).then(res=>{
					console.log("发送成功");
				}).catch(err=>{
					console.log("发送失败")
				})
			}
		}
	}
</script>

<style>
</style>

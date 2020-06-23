<template>
	<div class="usercenter">
		用户中心
		<div v-if="userinfo">
			注册日期:{{userinfo.date_joined|dataForamt}}
			<div>
				<h2>修改信息</h2>
				<van-field v-model="userinfo.username" type="text" label="用户名" />
				<van-field v-model="userinfo.telephone" type="tel" label="手机号" />
				<van-field v-model="userinfo.password" type="password" label="密码" />
				<van-field v-model="userinfo.email" type="email" label="邮箱" />
				<van-button @click="modify" round block type="info" native-type="submit">
				     修改信息
				</van-button>
			</div>
		</div>
		
	</div>
</template>

<script>
	export default{
		data(){
			return{
				userinfo:null,		
			}
		},
		
		created() {
			this.$api.getUserInfo().then(res=>{
				console.log("请求个人信息",res);
				this.userinfo=res.data;
				this.$jsCookie.set("userinfo",res.data)
			}).catch(err=>{
				console.log("请求个人信息出错",err);
			})
		},
		
		methods:{
			modify(){
				console.log("请求修改个人信息");
				this.$api.modifyUserInfo({
					userinfo:this.userinfo
				}).then(res=>{
					console.log("更改成功",res);
				}).catch(err=>{
					console.log("更改出错",err);
				})
			}
		},
		filters:{
			dataForamt(date){
				date = new Date(date)
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		}
	
	
		
	}
	
</script>

<style>
</style>

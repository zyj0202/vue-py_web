<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
	<div class="categorys">
		<van-cell v-for="(item,index) in categorys" :title="item.name" is-link :to="'/categorys/'+item.id+'/'"/>
	</div>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<!-- <div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div> -->
	<div>
		<!-- <label for="">分类名</label> <input type="text" v-model="categoryName"> -->
		<van-field v-model="categoryName" label="分类名" placeholder="请输入分类名" />
		<br>
		<van-button round type="info" @click="requestCreateCategory">发起创建分类请求</van-button>
	</div>
	<!-- <div>
		<label for="">用户名:</label> <input type="text" v-model="username">
		<br>
		<label for="">密码:</label> <input type="text" v-model="password">
		<br>
		<button @click="requestToken">发起请求Token</button>
	</div>
	<div>
		<label for="">需要修改的分类的id</label>  <input type="text" v-model="newCategoryId">
		<br>
		<label for="">需要修改的分类名字</label> <input type="text" v-model="newCategoryName">
		<br>
		<button @click="requestModifyCategory">修改分类</button>
	</div> -->
	
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	  return{
		  categorys:[],
		  categoryName:"",
		  // newCategoryId:"",
		  // newCategoryName:""
	  }
  },
  components: {
    // HelloWorld
  },
  created() {
  	this.requestCategoryList();
  },
  methods:{
	  requestCategoryList(){
		  // console.log("点击了按钮")
		  
		  this.$api.getCategoryList().then(res=>{
			  console.log("请求分类列表",res)
			  if(res.status==200){
				  this.categorys = res.data;
			  }
			  
		  }).catch(err=>{
			  console.log("出错了",err)
		  })
		  // 获取分类列表
		  // this.$http({
			 //  method:'get',
			 //  url:'http://127.0.0.1:8000/api/v1/categorys/'
		  // }).then(res=>{
			 //  console.log("得到分类列表",res);
		  // }).catch(err=>{
			 //  console.log("发生错误",err);
		  // })
	  },
	  // requestToken(){
		 //  this.$api.getToken({
			//     username:this.username,
			//     password:this.password
		 //  }).then(res=>{
			//   console.log("请求Token令牌",res);
			//   this.$jsCookie.set("refresh",res.data.refresh);
			//   this.$jsCookie.set("access",res.data.access);
		 //  }).catch(err=>{
			//   console.log("出错了",err)
		 //  })
		 //  // this.$http({
			//  //  method:'post',
			//  //  url:'http://127.0.0.1:8000/obtaintoken/',
			//  //  data:{
			// 	//   username:this.username,
			// 	//   password:this.password
			//  //  }
		 //  // }).then(res=>{
			//  //  console.log("得到Token",res);
		 //  // }).catch(err=>{
			//  //  console.log("发生错误",err);
		 //  // })  
	  // },
	  requestCreateCategory(){
		  if(this.categoryName != ""){
			  this.$api.createCategory({
				  name:this.categoryName
			  }).then(res=>{
				  console.log("创建了分类",res);
				  this.categorys.push(res.data);
				  this.categoryName = "";
			  }).catch(err=>{
				  console.log("出错了",err)
			  })
			//   // this.$http({
			// 	 //  method:'post',
			// 	 //  url:'http://127.0.0.1:8000/api/v1/categorys/',
			// 	 //  data:{
			// 		//   name:this.categoryName
			// 	 //  },
			// 	 //  headers:{
			// 		//   // 使用Basic认证不安全
			// 		//   // Authorization:'Basic YWRtaW46MTIzNDU2'
			// 		//   Authorization:'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwNzQ0NTEwLCJqdGkiOiI0OWVkOTgyOWQwNjc0NDUwYmE0NmM4ZGNjOGJiNDg0ZiIsInVzZXJfaWQiOjN9.b8Tytj_ThGx7zQk2XI8zBPFdkU3ZV-gTRMLGv0uW3d8'
			// 	 //  }
			//   // }).then(res=>{
			// 	 //  console.log("创建结果",res);
			//   // }).catch(err=>{
			// 	 //  console.log("出错了",err);
			//   // })
		  }
		  else{
			  this.$toast("必须输入分类名");
			  console.log("必须输入分类名");
		  }
	  },
	  // requestModifyCategory(){
		 //  if(this.newCategoryId=="" || this.newCategoryName==""){
			//   console.log("需要选择分类并且重新给与名字");
		 //  }
		 //  else{
			//   this.$api.modifyCategory({
			// 	  id:this.newCategoryId,
			// 	  name:this.newCategoryName 
			//   }).then(res=>{
			// 	  console.log(res);
			//   }).catch(err=>{
			// 	  console.log(err);
			//   })
		 //  }
	  // }
	}
}
</script>

<!-- 浏览器默认的同源策略不允许跨域访问 域名和端口一致 -->
<!-- Access to XMLHttpRequest 
at 'http://127.0.0.1:8000/api/v1/categorys/' 
from origin 'http://localhost:8080' has been blocked by CORS policy: 
No 'Access-Control-Allow-Origin' header is present on the requested resource -->
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
import random
from .models import*
import razorpay 
from django.template.loader import render_to_string

# Create your views here.

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        
        try:
        
            uid=user.objects.get(email=email)
            if uid.email==email:
                messages.success(request,"Invalid email")
                return render(request,"register.html")
            else:
                return render(request,"register.html")
                
        except:
            if password==c_password:
                user.objects.create(name=name,
                                    email=email,
                                    password=password)

                messages.success(request,"data insert successfully")
                return render(request,"login.html")
            else:
                
                messages.success(request,"password not match")
                return render(request,"register.html")
                
    else:
        return render(request,"register.html")
        

def login(request):
    if "email" in request.session:
        return render(request,"index.html")
    try:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            
            uid=user.objects.get(email=email)
            if uid.email==email:
                if uid.password==password:
                    request.session["email"]=uid.email
                    messages.success(request,"succeessfully login")
                    return redirect("index")
                else:
                    messages.success(request,"Invalid password")
                    return render(request,"login.html")
            else:
                
                return render(request,"login.html")
                
        else:        
            return render(request,"login.html")
    except:
        messages.success(request,"Invalid email")
        return render(request,"login.html")
        
        
    
def logout(request):
    if "email" in request.session:
        del request.session ["email"]
        return render(request,"login.html")   
    else:
        return render(request,"login.html")   
           
def forget(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        
        try:
            uid=user.objects.get(email=email)
            uid.otp=otp
            uid.save()
            send_mail("forget password","your otp is "+str(otp),'gohiljayb10@gmail.com',[email])
            server={
                'email':email
            }
            return render(request,"confirm_password.html",server)
        except:
            messages.success(request,"Invalid email")
            return render(request,"forget.html")
    else:
        return render(request,"forget.html")
        
def confirm_password(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        con_password=request.POST['con_password']
        
        uid=user.objects.get(email=email)
        if str(uid.otp)==otp:
            if new_password==con_password:
                uid.password=new_password
                uid.save()

                return render(request,"login.html")
            else:
                server={
                    "email":email
                }
                return render(request,"confirm_password.html",server)
        
        else:
            server={
                "email":email
            }
            return render(request,"confirm_password.html",server)
    return render(request,"confirm_password.html")
                
                
      
def index(request):
    if "email" in request.session:
        mid=main_category.objects.all()
        pid1=product1.objects.filter(main_category=1)
        pid=product1.objects.filter(main_category=2)
        uid=user.objects.get(email=request.session['email'])
        sid=subcategory.objects.filter(main_category=2)
        sid1=subcategory.objects.filter(main_category=1)
        count=add_to_cart.objects.filter(user_id=uid).count() 
        count1=wishlist.objects.filter(user_id=uid).count() 
        pro=add_to_cart.objects.filter(user_id=uid)
        pro1=wishlist.objects.filter(user_id=uid)
        
        total=0
        sub_total=0
        l1=[]
        
        for i in pro:
            a=i.total
            l1.append(a)
            sub_total=sum(l1)
            total=sub_total
         
        total1=0
        sub_total1=0
        l11=[]
           
        for i in pro1:
            a=i.price
            l11.append(a)
            sub_total1=sum(l11)
            total1=sub_total1
              
        cid=request.GET.get('cid')
        did=request.GET.get('did')
        
        
        if cid:
            pid=product1.objects.filter(main_category=2,subcategory=cid)
        elif did:
            pid1=product1.objects.filter(main_category=1,subcategory=did)
        else:
           pid=product1.objects.filter(main_category=2)
           pid1=product1.objects.filter(main_category=1)
           
        contaxt={
            "mid":mid,
            "pid":pid,
            "pid1":pid1,
            "uid":uid,
            "sid":sid,
            "sid1":sid1,
            "count":count,
            "count1":count1,
            "total":total,
            "total1":total1,
            "pro":pro,
            "pro1":pro1
            
        }
        return render(request,"index.html",contaxt)
    else:
        return render(request,"login.html")

def blog_details(request):
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1

    contaxt={
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
        
    }
    
    return render(request,"blog-details.html",contaxt)

def blog(request):
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()

    mid=main_category.objects.all()
    
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    contaxt={
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
    }
    return render(request,"blog.html",contaxt)

def contact(request):
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        
        contactpage.objects.create(name=name,
                                email=email,
                                msg=msg)
        
        contaxt={
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
        
                    }
        return render(request,"contact.html",contaxt)
    else:
        contaxt={
            "count":count,
            "count1":count1,
            "mid":mid,
            "total":total,
            "total1":total1,
            "pro":pro,
            "pro1":pro1,
                        }
        return render(request,"contact.html",contaxt)
        

def faq(request):
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    contaxt={
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
    }
    return render(request,"faq.html",contaxt)

def main(request):
    return render(request,"main.html")

def product(request):
    show=add_to_cart.objects.all()
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    
    contaxt={
        'show':show,
        "count":count,
        "mid":mid,
    }
    return render(request,"product.html",contaxt)

def shop(request):
    mid=main_category.objects.all()
    pid=product1.objects.all()
    sid=subcategory.objects.all()
    bid=brand.objects.all()
    priceid=filter_price.objects.all()
    cid=color.objects.all()
    sizeid=size.objects.all()
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
    
    product_count=product1.objects.count()
    
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    scid=request.GET.get('cid')
    bcid=request.GET.get('bcid')
    pcid=request.GET.get('pcid')
    ccid=request.GET.get('ccid')
    seeid=request.GET.get('seeid')
    sid=request.GET.get('sort')
    
    if scid:
        pid=product1.objects.filter(subcategory=scid) 
    elif bcid:
        pid=product1.objects.filter(brand=bcid)  
    elif pcid:
        pid=product1.objects.filter(filter_price=pcid) 
    elif ccid:
        pid=product1.objects.filter(color=ccid)   
    elif seeid:
        pid=product1.objects.filter(size=seeid)
    elif sid=='lth':
        pid=product1.objects.all().order_by("price")
    elif sid=='htl':
        pid=product1.objects.all().order_by("-price") 
    elif sid=='atz':
        pid=product1.objects.all().order_by("name")  
    elif sid=='zta':
        pid=product1.objects.all().order_by("-name")             
    else:
        pid=product1.objects.all()   
    
    contaxt={
        "mid":mid,
        "pid":pid,
        "sid":sid,
        "bid":bid,
        "priceid":priceid,
        "cid":cid,
        "sizeid":sizeid,
        "count":count,
        "count1":count1,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
        "product_count":product_count,
        
    }
    return render(request,"shop.html",contaxt)

def shopping_cart(request):
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    
    mid=main_category.objects.all()
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    print(count)
    
    sub_total2=0
    total2=0
    l12=[]
    
    for i in pro:
        a=i.total
        l12.append(a)
        sub_total2=sum(l12)
        total2=sub_total2+50
        
    server={
        "pro":pro,
        "sub_total":sub_total,
        "total":total,
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "total2":total2,
        "pro":pro,
        "pro1":pro1,
        
    }
    
    return render(request,"shopping-cart.html",server)

def collection(request,id):
    mid=main_category.objects.all()
    pid=product1.objects.filter(main_category=id)
    uid=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()

    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    contaxt={
        "mid":mid,
        "pid":pid,
        "count":count,
        "count1":count1,

        "total":total,
        "total1":total1,
        "total":total,
        "pro":pro,
        "pro1":pro1,
    }
    return render(request,"collection.html",contaxt)
    
def sub_category(request):
    mid=main_category.objects.all()
    sid=sub_category.objects.filter(main_category=mid)
    contaxt={
        "mid":mid,
        "sid":sid,
    }
    return render(request,"index.html",contaxt)  

def cart(request,id):
    uid=user.objects.get(email=request.session['email'])
    product=product1.objects.get(id=id)
    pid=add_to_cart.objects.filter(product_id=product,user_id=uid).exists()
    
    
    
    if pid:
        cart=add_to_cart.objects.get(product_id=product)
        if cart.qtn < 10:
            cart.qtn += 1
            cart.total = cart.qtn * cart.price 
            cart.save()
            return redirect("shopping_cart")   
        else:
            return redirect("shopping_cart") 
    else:
        add_to_cart.objects.create(
                                    user_id=uid,
                                    product_id=product,
                                    image=product.image,
                                    pro_name=product.name,
                                    price=product.price,
                                    qtn=product.qtn,
                                    total=product.price)
        return redirect("shopping_cart")

def increment(request,id):
    cart=add_to_cart.objects.get(id=id)
    if cart.qtn < 10:
        cart.qtn += 1
        cart.total = cart.qtn * cart.price 
        cart.save()
        return redirect("shopping_cart")   
    else:
        return redirect("shopping_cart")   
         

def decrement(request,id):
    cart=add_to_cart.objects.get(id=id)
    if cart.qtn > 1:
        cart.qtn -= 1
        cart.total = cart.qtn * cart.price
        cart.save()
        return redirect("shopping_cart") 
    else:
        return redirect("shopping_cart") 
        

def remove(request,id):
    cart=add_to_cart.objects.get(id=id)
    
    cart.delete()
    
    return redirect("shopping_cart") 
   
def apply_coupon(request):
    uid=user.objects.get(email=request.session['email'])
    
    show=add_to_cart.objects.all() #index show cart
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    
    
    bid=billing_detail.objects.all()
    pro=add_to_cart.objects.filter(user_id=uid)
    cid=coupon.objects.get(code="abcd10")
    cid1=coupon.objects.get(code="akash10")

        
    sub_total2=0
    total2=0
    l12=[]
    
    
    for i in pro:
        a=i.total
        l12.append(a)
        sub_total2=sum(l12)
        total2=sub_total2 + 50 
        
        
    sub_total=0
    total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total+50
        
        
    if request.POST:
        code=request.POST['code']
        
    if cid.code==code:
        if sub_total >= cid.min_order_amount and sub_total <= cid.max_order_amount:
            print("valid coupon")
            total=total-cid.discount_amount
            contaxt={
            "uid":uid,
            "pro":pro,
            "sub_total":sub_total,
            "total":total,
            "cid":cid.discount_amount,
            "bid":bid,
            "show":show,
            "count":count,
            "count1":count1,
            "mid":mid,
            "total2":total2-cid.discount_amount,
            
        }
            messages.success(request,"coupon apply successfully")
            return render(request,"check-out.html",contaxt)
        else:
            contaxt={
            "uid":uid,
            "pro":pro,
            "sub_total":sub_total,
            "total":total,
            "bid":bid,
            "show":show,
            "count":count,
            "count1":count1,
            "mid":mid,
            "total2":total2,
            
            
            
        }
            messages.success(request,"Invalid coupon code")
            return render(request,"check-out.html",contaxt)
            
    
    elif cid1.code==code:
        if sub_total >= cid.min_order_amount and sub_total <= cid.max_order_amount:
        
            print("valid coupon")
            total=total-cid1.discount_amount
            contaxt={
            "uid":uid,
            "pro":pro,
            "sub_total":sub_total,
            "total":total,
            "cid1":cid1.discount_amount,
            "bid":bid,
            "show":show,
            # "count":count,
            "mid":mid,
            "total2":total2-cid1.discount_amount,
            
            
        }
            messages.success(request,"coupon apply successfully")
            
            return render(request,"check-out.html",contaxt)
        else:
            contaxt={
            "uid":uid,
            "pro":pro,
            "sub_total":sub_total, 
            "total":total,
            "bid":bid,
            "show":show,
            # "count":count,
            "mid":mid,
            "total2":total2,
            
            
            
        }
            messages.success(request,"Invalid coupon code")
            
            return render(request,"check-out.html",contaxt)
        
    
    else:
        contaxt={
        "uid":uid,
        "pro":pro,
        "sub_total":sub_total,
        "total":total,
        "bid":bid,
        "show":show,
        # "count":count,
        "mid":mid,
        "total2":total2,
        
        
        
    }
        messages.success(request,"Invalid coupon code")
        
        print("Invalid coupon")
        
        return render(request,"check-out.html",contaxt)
    
        
def check_out(request):
    show=add_to_cart.objects.all()
    read=coupon.objects.all()
    uid1=user.objects.get(email=request.session['email'])
    count=add_to_cart.objects.filter(user_id=uid1).count()
    count1=wishlist.objects.filter(user_id=uid1).count()
    mid=main_category.objects.all()
    pro=add_to_cart.objects.filter(user_id=uid1)
    pro1=wishlist.objects.filter(user_id=uid1)
    
    # place order
    
    
    # =======================================    
    # address 
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        

    
    
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
        
    bid=billing_detail.objects.filter(uid=uid1)
    sub_total2=0
    total2=0
    l12=[]
    
    
    for i in pro:
        a=i.total
        l12.append(a)
        sub_total2=sum(l12)
        total2=sub_total2 + 50
        
    try:    
        amount = total2*100#100 here means 1 dollar,1 rupree if currency INR
        client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
        response = client.order.create({'amount':amount,'currency':'INR','payment_capture':0})
        print(response,"**************")
     
    
        contaxt={
            "uid":uid1,
            "pro":pro,
            "sub_total":sub_total,
            "sub_total2":sub_total2,
            "total2":total2,
            "bid":bid,
            "read":read,
            "show":show,
            "count":count,
            "count1":count1,
            "mid":mid,
            "total":total,
            "total1":total1,
            "pro":pro,
            "pro1":pro1,
            "response":response,
            
        }
            
            
        return render(request,"check-out.html",contaxt)
    except:
        return render(request,"check-out.html")  
    
  

    
   
        
        

def order(request):
    uid=user.objects.get(email=request.session['email'])
    show1=orders.objects.filter(user_id=uid)
    show=add_to_cart.objects.all()
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    mid=main_category.objects.all()
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
    count=orders.objects.filter(user_id=uid).count()
    
    total0=0
    sub_total0=0
    l10=[]
    
    for i in show1:
        a=i.price * i.qtn
        l10.append(a)
        sub_total0=sum(l10)
        total0=sub_total0 + 50
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    contaxt={
        "show":show,
        "show1":show1,
        "count":count,
        "count1":count1,
        "mid":mid,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
        "total0":total0,
        
}
    return render(request,"order.html",contaxt)

def remove_order(request,id):
    or_der=orders.objects.get(id=id)
    
    or_der.delete()
    
    return redirect("order")

def placeorder(request):
    uid1=user.objects.get(email=request.session['email'])
    aid=add_to_cart.objects.filter(user_id=uid1)
    
    if request.POST:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        contry=request.POST['contry']
        address=request.POST['address']
        pincode=request.POST['pincode']
        city=request.POST['city']
        email=request.POST['email']
        phone=request.POST['phone']
            
        billing_detail.objects.create(uid=uid1,
                                      first_name=first_name,
                                      last_name=last_name,
                                      contry=contry,
                                      address=address,
                                      pincode=pincode,
                                      city=city,
                                      email=email,
                                      phone=phone)
        
    
    total=0
    l1=[]
    
    for i in aid:
        a=i.total
        l1.append(a)
        total=sum(l1)
        
    amount = total*100#100 here means 1 dollar,1 rupree if currency INR
    client = razorpay.Client(auth=('rzp_test_bilBagOBVTi4lE','77yKq3N9Wul97JVQcjtIVB5z'))
    response = client.order.create({'amount':amount,'currency':'INR','payment_capture':0})
    print(response,"**************")
    order_id=response['id']
    print(order_id)     
    
    for i in aid:
        
        orders.objects.create(user_id=uid1,
                            image=i.image,
                            product_name=i.pro_name,
                            price=i.price,
                            qtn=i.qtn,
                            order_id=order_id,
                            product_total=i.total,
                            total=total)
        
        i.delete()

    var=render_to_string("invoice.html")
                # subject                  #msg                  #email                       #uid
    send_mail("e-commerece website","Thank you for shopping","gohiljayb10@gmail.com",[request.session['email']],html_message=var)          
    
    contaxt={
        "response":response,
    }  
    
    return redirect("order")
    
        

def show_wishlist(request):
    uid=user.objects.get(email=request.session['email'])
    show1=wishlist.objects.filter(user_id=uid)
    show=add_to_cart.objects.all()
    mid=main_category.objects.all()
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
        
    total=0
    sub_total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    total1=0
    sub_total1=0
    l11=[]
        
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1
    
    
    contaxt={
        "show1":show1,
        "show":show,
        "mid":mid,
        "count":count,
        "count1":count1,
        "total":total,
        "total1":total1,
        "pro":pro,
        "pro1":pro1,
    }
    return render(request,"wishlist.html",contaxt)

def add_to_wishlist(request,id):
    uid=user.objects.get(email=request.session['email'])
    pid=product1.objects.get(id=id)
    show1=wishlist.objects.filter(user_id=uid,product_id=pid).exists()
    
    if show1:
        messages.success(request,"alreay exits product")
        return redirect("shop")
    else:
    
        wishlist.objects.create(user_id=uid,
                                product_id=pid,
                                image=pid.image,
                                name=pid.name,
                                price=pid.price)    
        
        return redirect("show_wishlist")

def wishlist_remove(request,id):
    wid=wishlist.objects.get(id=id)
    
    wid.delete()
    
    return redirect("show_wishlist")

def profile(request):
    uid=user.objects.get(email=request.session['email'])
    pro=add_to_cart.objects.filter(user_id=uid)
    pro1=wishlist.objects.filter(user_id=uid)
    mid=main_category.objects.all()
    
    count=add_to_cart.objects.filter(user_id=uid).count()
    count1=wishlist.objects.filter(user_id=uid).count()
    
    sub_total=0
    total=0
    l1=[]
    
    for i in pro:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total
        
    sub_total1=0
    total1=0
    l11=[]
    
    for i in pro1:
        a=i.price
        l11.append(a)
        sub_total1=sum(l11)
        total1=sub_total1

    if request.POST:
        name=request.POST['name'] 
        email=request.POST['email'] 
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        
        try:
        
            if uid.password==old_password:
                uid.password=new_password
                uid.save()
                
                contaxt={
                
                "uid":uid
            }
                messages.success(request,"password change successfuly")
                return redirect("profile")
            else:
                messages.success(request,"Invalid password")
                return redirect("profile")
        except:
           pass
        
        if "image" in request.FILES:
            image=request.FILES['image']
            uid.image=image
            uid.save()  
                 
        uid.name=name
        uid.email=email
        uid.save()
        
        contaxt={
            
            "uid":uid,
            "mid":mid,
            "count1":count1,
            "count":count,
            "total":total,
            "total1":total1,
            "pro":pro,
            "pro1":pro1
            
        }
    
        return render(request,"profile.html",contaxt)
    else:
        contaxt={
            
            "uid":uid,
            "mid":mid,
            "count1":count1,
            "count":count,
            "total":total,
            "total1":total1,
            "pro":pro,
            "pro1":pro1
            

        }
    
        return render(request,"profile.html",contaxt)
    
def search(request):
    search1=request.GET['search']
    if search1:
        pid=product1.objects.filter(name__contains=search1)
        
    contaxt={
        "pid":pid,
    }
    return render(request,"shop.html",contaxt)

def invoice(request):
    uid=user.objects.get(email=request.session['email'])
    show=orders.objects.filter(user_id=uid).order_by("-id")
    billing_show=billing_detail.objects.filter(uid=uid).order_by("-id")[0:1]
        
    # show sub_total and total
    
    sub_total=0
    total=0
    l1=[]
    
    for i in show:
        a=i.total
        l1.append(a)
        sub_total=sum(l1)
        total=sub_total+50
        
    contaxt={
        'show':show,
        "sub_total":sub_total,
        "total":total,
        "billing_show":billing_show,
    }
    
    return render(request,"invoice.html",contaxt)



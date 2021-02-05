My [theme](https://www.youtube.com/watch?v=NVGuFdX5guE) for 2021 is "year of creativity". For a while I've felt like I have a lot of creative ideas brewing in my head, but no idea how to even begin making them real. This year, I want to make real headway on this.

Eventually, I want to make real sound and music visualization that gets as close to synesthesia as humanly possible for those without synesthesia. But, baby steps. First, I want to find out how to generate beautiful, random images, like the ones that appear on my Twitter feed from [Arty](https://twitter.com/ArtyOriginals), [tweegeemee](https://twitter.com/tweegeemee), etc. Last week, I found [this article](https://bjbestpoet.wordpress.com/the-art-of-the-bot/) from the creator of the Arty bots that explained his journey from not knowing how to code to learning all about how to make beautiful generative art. In there, the creator says that [this article](https://jeremykun.com/2012/01/01/random-psychedelic-art/) was essential to his being able to get started. So, I read that article, and I spent many hours trying to understand the [full source code](https://github.com/j2kun/random-art/blob/main/randomart.py) for the program the person from that article wrote.

It's really interesting. It uses recursion to generate a long, random pattern of nested sine and cosine functions, and then solves the equation for each pixel to eventually create an image like this:

![example of random, psychedelic art generated by this program](https://cloud-giwd1tbtv.vercel.app/0img4.png)

One I figured out how it works, I thought: why stop at sine, cosine, and multiplication? I decided I was going to add tangent, arcsin, arccosine, arctangent, and division. So I spent a whole day doing that. It's actually a lot hader than it sounds—each randomly-generated value that you get from solving the nested equations must be in [-1, 1], so I had to dust off some of the calculus I learned in high school and implement the correct phase shifts for each function. That made some even cooler-looking images, like these:

<details>

<summary>Click to expand</summary>

![](https://cloud-cxq32dygu.vercel.app/0img1.png)
![](https://cloud-cxq32dygu.vercel.app/1img3.png)
![](https://cloud-cxq32dygu.vercel.app/2img4.png)
![](https://cloud-cxq32dygu.vercel.app/3img0.png)

</details>

For division, because it's basically impossible to prevent division by 0 from happening at some point, I made it so that if it does divide divide by 0, generate a random number betweeen -1 and 1 and use that instead. It turns out division by 0 happens _a lot_, so that, combined with the rest of the trig functions, generated some very cool noisy pictures:

<details>

<summary>Click to expand</summary>

![](https://cloud-6vtzfpf7q.vercel.app/0img0.png)
![](https://cloud-6vtzfpf7q.vercel.app/1img1.png)
![](https://cloud-6vtzfpf7q.vercel.app/2img4.png)

</details>

It's been really fun playing around with images and calculus! I'm really excited to dive deeper and make some more cool stuff. Eventually I want to make my own totally original thing that's not just adapted from someone else's source code. But for now I wanted to share my progress here.

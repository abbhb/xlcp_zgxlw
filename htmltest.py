
htmla = '''

<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="renderer" content="webkit">
<title>PSYTEST</title>
<link rel="stylesheet" href="//cdn.psy.com.cn/scripts/amazeui/css/amazeui.min.css">
<link rel="stylesheet" href="/lb/inc/test.css">
</head>

<body>
<div class="am-container">
  <article>
    <h1 class="am-text-xl lang">&nbsp;</h1>
    
    <div id="lb-zhidaoyu" class="am-text-sm">
      <span class="tts am-btn am-btn-default am-btn-xs am-btn-hollow" title="播放语音"></span>
      <span class="lang">这里有不少大家都感兴趣的问题，请你来回答。由于每个人对这些问题都会有自己的看法，回答起来一定是不会相同的，因而对这些问题的回答，并没有对与不对之分，只是表明每个人对这些问题的态度，请你不要有所顾虑，要尽量坦率地表达自己对这些问题的真实兴趣和态度。对测题不要费时间去考虑怎样答才对，因为无所谓对错，而要顺其自然，你是怎样想的和做的就怎样回答。注意：每一测题都要回答，不要有遗漏。每一测题只能选择一个答案，不许多选。必须在50分钟内回答完全部测题，请掌握好时间。</span>
    </div>
    
    <div id="lb-act">
      <form id="form">
        <input type="hidden" name="answer" id="answer">
        <input type="hidden" name="howlong" id="howlong">
        <input type="hidden" name="lb" id="lb" value="1">
        <input type="hidden" name="attach" id="attach">
      </form>
      <input type="button" class="am-btn am-btn-success am-btn-sm btn-start" value="开始">
      <input type="button" class="am-btn am-btn-success am-btn-sm btn-end" value="做完了" disabled>
      <select id="select-lang" data-am-selected="{btnWidth:'85px',btnSize:'xs',btnStyle:'success',maxHeight:'200px'}">
        
        <option value="zh">中文</option>
        
        <option value="en">英语</option>
        
        <option value="ja">日语</option>
        
        <option value="ko">韩语</option>
        
        <option value="fr">法语</option>
        
        <option value="es">西班牙语</option>
        
        <option value="it">意大利语</option>
        
        <option value="de">德语</option>
        
        <option value="tr">土耳其语</option>
        
        <option value="ru">俄语</option>
        
        <option value="pt">葡萄牙语</option>
        
        <option value="vi">越南语</option>
        
        <option value="th">泰语</option>
        
        <option value="ms">马来语</option>
        
      </select>
      <input type="hidden" id="name" value="测一测你的人格特质是什么样的？">
      <input type="hidden" id="maxid" value="140">
      <input type="hidden" id="mintime" value="5">
      <input type="hidden" id="maxtime" value="40">
      <input type="hidden" id="preview" value="">
    </div>
    <div id="testing" class="am-cf">
      <span id="testing-time" class="am-badge am-badge-warning am-round am-fl am-margin-right-xs">0:0:0</span>
      <span id="testing-number" class="am-badge am-badge-warning am-round am-fl am-margin-right-xs">1/140</span>
      <div id="testing-progress"></div>
    </div>
    <form id="form-question" class="am-form">
      
      <div class="q am-panel am-panel-default" id="q_1">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_1'></span>1. <span class='lang'>你愿意自己玩，还是愿意和朋友一起玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-1' id='a-1-1' value='1' data-am-ucheck><span class='lang'>自己玩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-1' id='a-1-2' value='2' data-am-ucheck><span class='lang'>和朋友一起玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_2">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_2'></span>2. <span class='lang'>“着急”这个词的意思是与“冷静”相反，还是与“困倦”、“担心”相反？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-2' id='a-2-1' value='1' data-am-ucheck><span class='lang'>冷静</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-2' id='a-2-2' value='2' data-am-ucheck><span class='lang'>困倦</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-2' id='a-2-3' value='3' data-am-ucheck><span class='lang'>担心</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_3">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_3'></span>3. <span class='lang'>你们班的多数同学都喜欢你，还是只有几个同学喜欢你？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-3' id='a-3-1' value='1' data-am-ucheck><span class='lang'>多数同学喜欢我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-3' id='a-3-2' value='2' data-am-ucheck><span class='lang'>只有几个同学喜欢我</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_4">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_4'></span>4. <span class='lang'>当听到有人说你的坏话时，你经常平静地跟他说理，还是感到非常恼火？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-4' id='a-4-1' value='1' data-am-ucheck><span class='lang'>平静地说理</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-4' id='a-4-2' value='2' data-am-ucheck><span class='lang'>非常恼火</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_5">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_5'></span>5. <span class='lang'>你认为你的家庭好，还是不如大多数同学的家庭好？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-5' id='a-5-1' value='1' data-am-ucheck><span class='lang'>不如大多数同学的家庭好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-5' id='a-5-2' value='2' data-am-ucheck><span class='lang'>我的家庭好</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_6">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_6'></span>6. <span class='lang'>你愿意当一名工程师，还是当一名飞机驾驶员？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-6' id='a-6-1' value='1' data-am-ucheck><span class='lang'>工程师</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-6' id='a-6-2' value='2' data-am-ucheck><span class='lang'>飞机驾驶员</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_7">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_7'></span>7. <span class='lang'>你喜欢过繁华的马路，还是不敢过？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-7' id='a-7-1' value='1' data-am-ucheck><span class='lang'>喜欢过</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-7' id='a-7-2' value='2' data-am-ucheck><span class='lang'>不敢过</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_8">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_8'></span>8. <span class='lang'>你用的东西坏了的时候，总是找别人给修理，还是喜欢自己动手修理？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-8' id='a-8-1' value='1' data-am-ucheck><span class='lang'>找别人给修理</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-8' id='a-8-2' value='2' data-am-ucheck><span class='lang'>自己动手修理</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_9">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_9'></span>9. <span class='lang'>在复习功课时，你喜欢老师给讲解，还是喜欢自己复习？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-9' id='a-9-1' value='1' data-am-ucheck><span class='lang'>喜欢老师给讲解</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-9' id='a-9-2' value='2' data-am-ucheck><span class='lang'>喜欢自己复习</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_10">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_10'></span>10. <span class='lang'>你在班里经常是安安静静的，还是想说什么就说什么？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-10' id='a-10-1' value='1' data-am-ucheck><span class='lang'>安安静静的</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-10' id='a-10-2' value='2' data-am-ucheck><span class='lang'>想说什么就说什么</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_11">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_11'></span>11. <span class='lang'>对老师要求做的工作，你经常做得很好，还是不如别的同学做得好？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-11' id='a-11-1' value='1' data-am-ucheck><span class='lang'>做得很好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-11' id='a-11-2' value='2' data-am-ucheck><span class='lang'>不如别的同学做得好</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_12">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_12'></span>12. <span class='lang'>你在听收音机或看电视时，别人在身旁讲话，对你有影响，还是他们讲他们的，你听你的？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-12' id='a-12-1' value='1' data-am-ucheck><span class='lang'>对我有影响</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-12' id='a-12-2' value='2' data-am-ucheck><span class='lang'>他们讲他们的，我听我的</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_13">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_13'></span>13. <span class='lang'>你上学如果迟到了，你会感到不好意思，还是觉得没有什么？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-13' id='a-13-1' value='1' data-am-ucheck><span class='lang'>不好意思</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-13' id='a-13-2' value='2' data-am-ucheck><span class='lang'>没有什么</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_14">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_14'></span>14. <span class='lang'>当有人提议做某件事情时，你总是响应号召，还是总要问一问为什么要那样做？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-14' id='a-14-1' value='1' data-am-ucheck><span class='lang'>总是响应号召</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-14' id='a-14-2' value='2' data-am-ucheck><span class='lang'>总要问一问为什么</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_15">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_15'></span>15. <span class='lang'>如果你有闲暇时间的话，你是愿意到外面去玩一玩，还是愿意在家里读一本有意思的书？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-15' id='a-15-1' value='1' data-am-ucheck><span class='lang'>到外面去玩一玩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-15' id='a-15-2' value='2' data-am-ucheck><span class='lang'>在家里读一本有意思的书</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_16">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_16'></span>16. <span class='lang'>当你见到你的朋友打架的时候，你是尽量把他们拉开，还是不管？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-16' id='a-16-1' value='1' data-am-ucheck><span class='lang'>拉开</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-16' id='a-16-2' value='2' data-am-ucheck><span class='lang'>不管</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_17">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_17'></span>17. <span class='lang'>你做作业时，经常做完后再检查一遍，还是做完了事？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-17' id='a-17-1' value='1' data-am-ucheck><span class='lang'>再检查一遍</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-17' id='a-17-2' value='2' data-am-ucheck><span class='lang'>做完了事</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_18">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_18'></span>18. <span class='lang'>你总觉得有些人不喜欢你，还是觉得多数人喜欢你？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-18' id='a-18-1' value='1' data-am-ucheck><span class='lang'>总觉得有些人不喜欢我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-18' id='a-18-2' value='2' data-am-ucheck><span class='lang'>觉得多数人喜欢我</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_19">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_19'></span>19. <span class='lang'>当需要你对妈妈讲一讲学校里的事情，又有一个展览会让你去参观，你是留在家讲事，还是参观展览会？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-19' id='a-19-1' value='1' data-am-ucheck><span class='lang'>在家里讲学校里的事情</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-19' id='a-19-2' value='2' data-am-ucheck><span class='lang'>去参观展览会</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_20">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_20'></span>20. <span class='lang'>你认为，你是一个有礼貌的孩子，还是有些调皮？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-20' id='a-20-1' value='1' data-am-ucheck><span class='lang'>有礼貌</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-20' id='a-20-2' value='2' data-am-ucheck><span class='lang'>有些调皮</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_21">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_21'></span>21. <span class='lang'>当你见到邻居家小孩哭的时候，你总是想办法把他哄好，还是把他送到他母亲那儿去？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-21' id='a-21-1' value='1' data-am-ucheck><span class='lang'>想办法哄好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-21' id='a-21-2' value='2' data-am-ucheck><span class='lang'>送给他母亲</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_22">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_22'></span>22. <span class='lang'>“帮助与妨碍”的关系好比“允许与拒绝”的关系还是“允许与惩罚”、“允许与禁止”的关系？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-22' id='a-22-1' value='1' data-am-ucheck><span class='lang'>允许与拒绝</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-22' id='a-22-2' value='2' data-am-ucheck><span class='lang'>允许与惩罚</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-22' id='a-22-3' value='3' data-am-ucheck><span class='lang'>允许与禁止</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_23">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_23'></span>23. <span class='lang'>如果有商场售货员与打字员两种职业让你选择，你愿意做什么工作？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-23' id='a-23-1' value='1' data-am-ucheck><span class='lang'>商场售货员</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-23' id='a-23-2' value='2' data-am-ucheck><span class='lang'>打字员</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_24">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_24'></span>24. <span class='lang'>在你的生活中，你觉得没有什么困难的事儿，还是觉得有很多困难？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-24' id='a-24-1' value='1' data-am-ucheck><span class='lang'>没有多少困难</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-24' id='a-24-2' value='2' data-am-ucheck><span class='lang'>有很多困难</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_25">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_25'></span>25. <span class='lang'>你做事情比别人快，还是比别人慢？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-25' id='a-25-1' value='1' data-am-ucheck><span class='lang'>比别人快</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-25' id='a-25-2' value='2' data-am-ucheck><span class='lang'>比别人慢</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_26">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_26'></span>26. <span class='lang'>你用铅笔的时候，喜欢咬铅笔，还是不喜欢？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-26' id='a-26-1' value='1' data-am-ucheck><span class='lang'>喜欢咬</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-26' id='a-26-2' value='2' data-am-ucheck><span class='lang'>不喜欢咬</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_27">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_27'></span>27. <span class='lang'>你认为每个人都应该有自己的汽车，还是认为每家有自行车就行了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-27' id='a-27-1' value='1' data-am-ucheck><span class='lang'>有自己的汽车</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-27' id='a-27-2' value='2' data-am-ucheck><span class='lang'>有自行车就行了</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_28">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_28'></span>28. <span class='lang'>你需要买东西的时候，愿意自己去买，还是希望爸爸妈妈陪你去买？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-28' id='a-28-1' value='1' data-am-ucheck><span class='lang'>自己去买</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-28' id='a-28-2' value='2' data-am-ucheck><span class='lang'>爸爸妈妈陪着去买</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_29">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_29'></span>29. <span class='lang'>在你生气的时候，总是气得说不出话来，还是大声叫嚷？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-29' id='a-29-1' value='1' data-am-ucheck><span class='lang'>说不出话来</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-29' id='a-29-2' value='2' data-am-ucheck><span class='lang'>大声叫嚷</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_30">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_30'></span>30. <span class='lang'>当你家里有东西需要卖时，是你自己拿去卖，还是不敢去卖？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-30' id='a-30-1' value='1' data-am-ucheck><span class='lang'>自己去卖</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-30' id='a-30-2' value='2' data-am-ucheck><span class='lang'>不敢去卖</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_31">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_31'></span>31. <span class='lang'>将来你想当一名工人或一般工作人员就满意了，还是非当专家、领导不可？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-31' id='a-31-1' value='1' data-am-ucheck><span class='lang'>当一名工人或一般工作人员</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-31' id='a-31-2' value='2' data-am-ucheck><span class='lang'>非当专家、领导不可</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_32">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_32'></span>32. <span class='lang'>你觉得你家大人都很理解你？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-32' id='a-32-1' value='1' data-am-ucheck><span class='lang'>很理解我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-32' id='a-32-2' value='2' data-am-ucheck><span class='lang'>很不理解我</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_33">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_33'></span>33. <span class='lang'>为了感谢妈妈对你的照顾，你是想送点礼物表示你的心意，还是帮妈妈干点活，把房间打扫得干干净净？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-33' id='a-33-1' value='1' data-am-ucheck><span class='lang'>送礼物</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-33' id='a-33-2' value='2' data-am-ucheck><span class='lang'>干点活</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_34">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_34'></span>34. <span class='lang'>你喜欢听关于一台新机器的故事，还是喜欢听关于一位将军的故事？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-34' id='a-34-1' value='1' data-am-ucheck><span class='lang'>新机器的故事</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-34' id='a-34-2' value='2' data-am-ucheck><span class='lang'>将军的故事</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_35">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_35'></span>35. <span class='lang'>你和大人在一起的时候，你是愿意跟他们闲谈，还是愿意给他们表演一个节目？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-35' id='a-35-1' value='1' data-am-ucheck><span class='lang'>闲谈</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-35' id='a-35-2' value='2' data-am-ucheck><span class='lang'>表演节目</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_36">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_36'></span>36. <span class='lang'>你有时感到人们都不接近你，还是从来没有这种感觉？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-36' id='a-36-1' value='1' data-am-ucheck><span class='lang'>有时感到人们都不接近我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-36' id='a-36-2' value='2' data-am-ucheck><span class='lang'>从来没有这种感觉</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_37">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_37'></span>37. <span class='lang'>你喜欢跟朋友一起去野游，还是喜欢跟爸爸妈妈一块去野游？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-37' id='a-37-1' value='1' data-am-ucheck><span class='lang'>跟朋友一起去野游</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-37' id='a-37-2' value='2' data-am-ucheck><span class='lang'>跟爸爸妈妈一块去野游</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_38">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_38'></span>38. <span class='lang'>如果你犯了错误，你会长时间地烦恼，还是很快就忘了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-38' id='a-38-1' value='1' data-am-ucheck><span class='lang'>长时间地烦恼</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-38' id='a-38-2' value='2' data-am-ucheck><span class='lang'>很快就忘了</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_39">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_39'></span>39. <span class='lang'>你在暑假里，是想起什么就做什么，还是每天都有计划地工作和学习？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-39' id='a-39-1' value='1' data-am-ucheck><span class='lang'>想起什么就做什么</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-39' id='a-39-2' value='2' data-am-ucheck><span class='lang'>每天都有计划</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_40">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_40'></span>40. <span class='lang'>你喜欢早睡早起，还是喜欢睡懒觉？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-40' id='a-40-1' value='1' data-am-ucheck><span class='lang'>早睡早起</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-40' id='a-40-2' value='2' data-am-ucheck><span class='lang'>睡懒觉</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_41">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_41'></span>41. <span class='lang'>当有的同学在讲述一件你比他更熟悉的事情时，你是想表示你比他了解得更多，还是只听他讲？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-41' id='a-41-1' value='1' data-am-ucheck><span class='lang'>表示比他了解得更多</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-41' id='a-41-2' value='2' data-am-ucheck><span class='lang'>只听他讲</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_42">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_42'></span>42. <span class='lang'>2、4、8的下一个数是10、16、还是12？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-42' id='a-42-1' value='1' data-am-ucheck><span class='lang'>10</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-42' id='a-42-2' value='2' data-am-ucheck><span class='lang'>16</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-42' id='a-42-3' value='3' data-am-ucheck><span class='lang'>12</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_43">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_43'></span>43. <span class='lang'>当有的同学不和你一起玩时，你是感到很不舒服，还是无所谓，再去找别的同学玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-43' id='a-43-1' value='1' data-am-ucheck><span class='lang'>很不舒服</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-43' id='a-43-2' value='2' data-am-ucheck><span class='lang'>找别的同学玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_44">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_44'></span>44. <span class='lang'>当你妈妈的意见跟你的不一致时，你是经常敢跟她顶嘴，还是不敢顶嘴？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-44' id='a-44-1' value='1' data-am-ucheck><span class='lang'>经常顶嘴</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-44' id='a-44-2' value='2' data-am-ucheck><span class='lang'>不敢顶嘴</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_45">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_45'></span>45. <span class='lang'>你做事情经常很有信心，还是不那么有把握？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-45' id='a-45-1' value='1' data-am-ucheck><span class='lang'>很有信心</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-45' id='a-45-2' value='2' data-am-ucheck><span class='lang'>不那么有把握</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_46">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_46'></span>46. <span class='lang'>当有人问你愿意不愿意做某件事情时，你是很快就做出决定，还是很难决定？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-46' id='a-46-1' value='1' data-am-ucheck><span class='lang'>很快就做出决定</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-46' id='a-46-2' value='2' data-am-ucheck><span class='lang'>很难决定</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_47">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_47'></span>47. <span class='lang'>你愿意穿上一件漂亮的衣服让人们喜欢看你，还是不喜欢人们看你？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-47' id='a-47-1' value='1' data-am-ucheck><span class='lang'>喜欢人们看我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-47' id='a-47-2' value='2' data-am-ucheck><span class='lang'>不喜欢人们看我</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_48">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_48'></span>48. <span class='lang'>在夜间你害怕黑暗的地方，还是认为黑暗没有什么可怕的？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-48' id='a-48-1' value='1' data-am-ucheck><span class='lang'>害怕黑暗</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-48' id='a-48-2' value='2' data-am-ucheck><span class='lang'>黑暗没有什么可怕的</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_49">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_49'></span>49. <span class='lang'>当妈妈生你的气的时候，你会感到很难过，还是很快就忘了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-49' id='a-49-1' value='1' data-am-ucheck><span class='lang'>很难过</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-49' id='a-49-2' value='2' data-am-ucheck><span class='lang'>很快就忘了</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_50">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_50'></span>50. <span class='lang'>你跟不认识的人在一起时，你敢主动跟他们讲话，还是不敢讲？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-50' id='a-50-1' value='1' data-am-ucheck><span class='lang'>敢主动讲话</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-50' id='a-50-2' value='2' data-am-ucheck><span class='lang'>不敢讲</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_51">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_51'></span>51. <span class='lang'>当你们班新转来一名同学时，你愿意主动地去帮助他，还是让别人去帮助他？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-51' id='a-51-1' value='1' data-am-ucheck><span class='lang'>我主动帮助他</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-51' id='a-51-2' value='2' data-am-ucheck><span class='lang'>让别人帮助</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_52">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_52'></span>52. <span class='lang'>你和大人在一起时，总是大人们自己讲话不理你，还是大人们常常听你说话？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-52' id='a-52-1' value='1' data-am-ucheck><span class='lang'>大人们自己讲话</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-52' id='a-52-2' value='2' data-am-ucheck><span class='lang'>常常听我说话</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_53">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_53'></span>53. <span class='lang'>班里要选几名同学参加一项活动，如果你没有被选上，你总是抱怨，还是不在乎？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-53' id='a-53-1' value='1' data-am-ucheck><span class='lang'>抱怨</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-53' id='a-53-2' value='2' data-am-ucheck><span class='lang'>不在乎</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_54">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_54'></span>54. <span class='lang'>你愿意有一只小狗，还是愿意有一套乒乓球用具？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-54' id='a-54-1' value='1' data-am-ucheck><span class='lang'>有一只小狗</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-54' id='a-54-2' value='2' data-am-ucheck><span class='lang'>有一套乒乓球用具</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_55">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_55'></span>55. <span class='lang'>你愿意看童话故事的电影，还是愿意看描写成人生活的电影？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-55' id='a-55-1' value='1' data-am-ucheck><span class='lang'>童话故事的电影</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-55' id='a-55-2' value='2' data-am-ucheck><span class='lang'>描写成人生活的电影</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_56">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_56'></span>56. <span class='lang'>在做一项新工作时，你比别人做得快，还是不如别人快？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-56' id='a-56-1' value='1' data-am-ucheck><span class='lang'>比别人快</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-56' id='a-56-2' value='2' data-am-ucheck><span class='lang'>不如别人快</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_57">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_57'></span>57. <span class='lang'>当你开始做一项新工作时，你是愿意一口气把它做完，还是留下一部分以后干？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-57' id='a-57-1' value='1' data-am-ucheck><span class='lang'>一口气做完</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-57' id='a-57-2' value='2' data-am-ucheck><span class='lang'>留下一部分以后干</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_58">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_58'></span>58. <span class='lang'>你每天过得很愉快，还是总觉得要出什么事？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-58' id='a-58-1' value='1' data-am-ucheck><span class='lang'>过得很愉快</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-58' id='a-58-2' value='2' data-am-ucheck><span class='lang'>总觉得要出什么事</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_59">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_59'></span>59. <span class='lang'>在快要放学的时候，你仍然能安静地坐着学习，还是坐不住？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-59' id='a-59-1' value='1' data-am-ucheck><span class='lang'>能安静地学习</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-59' id='a-59-2' value='2' data-am-ucheck><span class='lang'>坐不住</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_60">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_60'></span>60. <span class='lang'>早晨起来是你自己收拾好床，还是让你妈妈帮你收拾？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-60' id='a-60-1' value='1' data-am-ucheck><span class='lang'>自己收拾</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-60' id='a-60-2' value='2' data-am-ucheck><span class='lang'>让妈妈收拾</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_61">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_61'></span>61. <span class='lang'>你每天都觉得有新鲜事情，还是感到平平淡淡？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-61' id='a-61-1' value='1' data-am-ucheck><span class='lang'>有新鲜事情</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-61' id='a-61-2' value='2' data-am-ucheck><span class='lang'>平平淡淡</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_62">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_62'></span>62. <span class='lang'>在“许多”、“坏的”、“大量的”、“很少”这些词中，哪一个词与其他词不是一类？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-62' id='a-62-1' value='1' data-am-ucheck><span class='lang'>大量的</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-62' id='a-62-2' value='2' data-am-ucheck><span class='lang'>很少</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-62' id='a-62-3' value='3' data-am-ucheck><span class='lang'>坏的</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_63">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_63'></span>63. <span class='lang'>老师想让你去组织一次班级活动，你愿意去组织，还是希望别人去组织？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-63' id='a-63-1' value='1' data-am-ucheck><span class='lang'>我去组织</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-63' id='a-63-2' value='2' data-am-ucheck><span class='lang'>别人去组织</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_64">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_64'></span>64. <span class='lang'>当你听到别人讲一个好消息的时候，你经常是安安静静地听，还是高兴得手舞足蹈？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-64' id='a-64-1' value='1' data-am-ucheck><span class='lang'>安安静静地听</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-64' id='a-64-2' value='2' data-am-ucheck><span class='lang'>高兴得手舞足蹈</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_65">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_65'></span>65. <span class='lang'>当别人托你办一件重要事情时，你往往把它忘掉，还是忘不了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-65' id='a-65-1' value='1' data-am-ucheck><span class='lang'>往往忘掉</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-65' id='a-65-2' value='2' data-am-ucheck><span class='lang'>忘不了</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_66">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_66'></span>66. <span class='lang'>你在班里总是安安静静地学习，还是好讲话？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-66' id='a-66-1' value='1' data-am-ucheck><span class='lang'>安安静静地学习</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-66' id='a-66-2' value='2' data-am-ucheck><span class='lang'>好讲话</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_67">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_67'></span>67. <span class='lang'>你每次考试总认为自己答得不错，还是不那么有把握？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-67' id='a-67-1' value='1' data-am-ucheck><span class='lang'>认为自己答得不错</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-67' id='a-67-2' value='2' data-am-ucheck><span class='lang'>不那么有把握</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_68">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_68'></span>68. <span class='lang'>你愿意学弹琴，还是愿意学开汽车？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-68' id='a-68-1' value='1' data-am-ucheck><span class='lang'>愿意学弹琴</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-68' id='a-68-2' value='2' data-am-ucheck><span class='lang'>愿意学开汽车</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_69">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_69'></span>69. <span class='lang'>你和同学们做游戏的时候，你是愿意做什么就做什么，还是愿意玩多数人玩的游戏？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-69' id='a-69-1' value='1' data-am-ucheck><span class='lang'>愿意做什么就做什么</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-69' id='a-69-2' value='2' data-am-ucheck><span class='lang'>愿意玩多数人玩的游戏</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_70">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_70'></span>70. <span class='lang'>你常常担心自己受惩罚，还是不担心？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-70' id='a-70-1' value='1' data-am-ucheck><span class='lang'>常常担心</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-70' id='a-70-2' value='2' data-am-ucheck><span class='lang'>不担心</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_71">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_71'></span>71. <span class='lang'>你在听广播时，坚持听新闻节目，还是一听到新闻节目就去玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-71' id='a-71-1' value='1' data-am-ucheck><span class='lang'>坚持听新闻节目</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-71' id='a-71-2' value='2' data-am-ucheck><span class='lang'>不愿听新闻节目</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_72">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_72'></span>72. <span class='lang'>你总是担心自己得不到好成绩，还是坚信自己一定会得到好成绩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-72' id='a-72-1' value='1' data-am-ucheck><span class='lang'>担心得不到好成绩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-72' id='a-72-2' value='2' data-am-ucheck><span class='lang'>坚信能得到好成绩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_73">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_73'></span>73. <span class='lang'>如果你有机会的话，你愿意逛一次公园，还是看一场拳击比赛？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-73' id='a-73-1' value='1' data-am-ucheck><span class='lang'>逛公园</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-73' id='a-73-2' value='2' data-am-ucheck><span class='lang'>看拳击比赛</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_74">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_74'></span>74. <span class='lang'>当你对某一问题和同学们不一样时，你是愿意把它说出来，还是不愿意说出自己的看法？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-74' id='a-74-1' value='1' data-am-ucheck><span class='lang'>把它说出来</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-74' id='a-74-2' value='2' data-am-ucheck><span class='lang'>不愿意说出来</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_75">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_75'></span>75. <span class='lang'>做事情的时候，你是喜欢按老师说的办法去做，还是喜欢按自己认为最好的办法去做？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-75' id='a-75-1' value='1' data-am-ucheck><span class='lang'>按老师说的做</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-75' id='a-75-2' value='2' data-am-ucheck><span class='lang'>按自己认为好的做</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_76">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_76'></span>76. <span class='lang'>当你妈妈不高兴时，你常常和她一样不高兴，还是想办法让妈妈高兴起来？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-76' id='a-76-1' value='1' data-am-ucheck><span class='lang'>和妈妈一样不高兴</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-76' id='a-76-2' value='2' data-am-ucheck><span class='lang'>想办法让妈妈高兴起来</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_77">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_77'></span>77. <span class='lang'>夜间星星向你眨眼睛，你觉得它是在笑，还是觉得看起来冷冰冰的很远？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-77' id='a-77-1' value='1' data-am-ucheck><span class='lang'>在笑</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-77' id='a-77-2' value='2' data-am-ucheck><span class='lang'>冷冰冰的很远</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_78">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_78'></span>78. <span class='lang'>你愿意当一名演员，还是当一名科学家？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-78' id='a-78-1' value='1' data-am-ucheck><span class='lang'>演员</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-78' id='a-78-2' value='2' data-am-ucheck><span class='lang'>科学家</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_79">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_79'></span>79. <span class='lang'>你觉得学校里的纪律太严了，还是觉得学校里的生活很有趣？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-79' id='a-79-1' value='1' data-am-ucheck><span class='lang'>学校纪律太严</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-79' id='a-79-2' value='2' data-am-ucheck><span class='lang'>学校生活很有趣</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_80">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_80'></span>80. <span class='lang'>当别人取笑你的时候，你是非常生气而大喊大叫，还是走开不理他们？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-80' id='a-80-1' value='1' data-am-ucheck><span class='lang'>非常生气而大喊大叫</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-80' id='a-80-2' value='2' data-am-ucheck><span class='lang'>走开不理他们</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_81">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_81'></span>81. <span class='lang'>你对别人的名字，很容易把它记住，还是容易忘掉？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-81' id='a-81-1' value='1' data-am-ucheck><span class='lang'>容易记住</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-81' id='a-81-2' value='2' data-am-ucheck><span class='lang'>容易忘掉</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_82">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_82'></span>82. <span class='lang'>如果李伟的爸爸就是你爸爸的哥哥，那么李伟和你是什么关系？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-82' id='a-82-1' value='1' data-am-ucheck><span class='lang'>李伟是我大伯</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-82' id='a-82-2' value='2' data-am-ucheck><span class='lang'>李伟是我叔叔</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-82' id='a-82-3' value='3' data-am-ucheck><span class='lang'>李伟是我哥哥</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_83">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_83'></span>83. <span class='lang'>你妈妈老是埋怨你做事太慢，还是夸奖你做事很快？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-83' id='a-83-1' value='1' data-am-ucheck><span class='lang'>埋怨我做事太慢</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-83' id='a-83-2' value='2' data-am-ucheck><span class='lang'>夸奖我做事很快</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_84">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_84'></span>84. <span class='lang'>“怕羞”一词的意思是与“勇敢”相反，还是与“大胆”，“胆小”相反？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-84' id='a-84-1' value='1' data-am-ucheck><span class='lang'>勇敢</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-84' id='a-84-2' value='2' data-am-ucheck><span class='lang'>大胆</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-84' id='a-84-3' value='3' data-am-ucheck><span class='lang'>胆小</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_85">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_85'></span>85. <span class='lang'>你在生气的时候，好噘着嘴或者哭，还是好分辨是非？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-85' id='a-85-1' value='1' data-am-ucheck><span class='lang'>噘着嘴或者哭</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-85' id='a-85-2' value='2' data-am-ucheck><span class='lang'>好分辨是非</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_86">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_86'></span>86. <span class='lang'>多数同学认为你的脾气不好，还是认为你很容易相处？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-86' id='a-86-1' value='1' data-am-ucheck><span class='lang'>认为我脾气不好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-86' id='a-86-2' value='2' data-am-ucheck><span class='lang'>认为我很容易相处</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_87">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_87'></span>87. <span class='lang'>当妈妈生你的气的时候，你总是感到很应该，还是委屈得想哭？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-87' id='a-87-1' value='1' data-am-ucheck><span class='lang'>感到很应该</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-87' id='a-87-2' value='2' data-am-ucheck><span class='lang'>委屈得想哭</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_88">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_88'></span>88. <span class='lang'>当你需要到医院看病时，你害怕去，还是把医院不当回事？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-88' id='a-88-1' value='1' data-am-ucheck><span class='lang'>害怕去医院</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-88' id='a-88-2' value='2' data-am-ucheck><span class='lang'>把去医院不当回事</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_89">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_89'></span>89. <span class='lang'>你愿意当一名汽车司机，还是当一名医生？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-89' id='a-89-1' value='1' data-am-ucheck><span class='lang'>当司机</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-89' id='a-89-2' value='2' data-am-ucheck><span class='lang'>当医生</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_90">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_90'></span>90. <span class='lang'>你常常感觉到同学们在笑话你，还是从来没有这种感觉？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-90' id='a-90-1' value='1' data-am-ucheck><span class='lang'>感到同学们在笑话我</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-90' id='a-90-2' value='2' data-am-ucheck><span class='lang'>没有这种感觉</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_91">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_91'></span>91. <span class='lang'>你在家里是主动干家务活，还是不愿干？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-91' id='a-91-1' value='1' data-am-ucheck><span class='lang'>主动干家务活</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-91' id='a-91-2' value='2' data-am-ucheck><span class='lang'>不愿干家务活</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_92">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_92'></span>92. <span class='lang'>你愿意跟爸爸妈妈去玩，还是愿意跟朋友去玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-92' id='a-92-1' value='1' data-am-ucheck><span class='lang'>跟爸爸妈妈去玩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-92' id='a-92-2' value='2' data-am-ucheck><span class='lang'>跟朋友去玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_93">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_93'></span>93. <span class='lang'>你愿意玩羽毛球，还是愿意玩篮球？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-93' id='a-93-1' value='1' data-am-ucheck><span class='lang'>愿意玩羽毛球</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-93' id='a-93-2' value='2' data-am-ucheck><span class='lang'>愿意玩篮球</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_94">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_94'></span>94. <span class='lang'>在很多同学们一块研究事的时候，你的主意常常比别人高明，还是不如别人？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-94' id='a-94-1' value='1' data-am-ucheck><span class='lang'>比别人高明</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-94' id='a-94-2' value='2' data-am-ucheck><span class='lang'>不如别人</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_95">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_95'></span>95. <span class='lang'>在争论某件事情时，你喜欢争论到底，还是尽快停止争论？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-95' id='a-95-1' value='1' data-am-ucheck><span class='lang'>争论到底</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-95' id='a-95-2' value='2' data-am-ucheck><span class='lang'>尽快停止争论</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_96">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_96'></span>96. <span class='lang'>当你遇到困难时，你常常感到没有希望，还是振着精神继续干下去？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-96' id='a-96-1' value='1' data-am-ucheck><span class='lang'>感到没有希望</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-96' id='a-96-2' value='2' data-am-ucheck><span class='lang'>振着精神干</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_97">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_97'></span>97. <span class='lang'>你和同学们一起做游戏的时候，你总是遵守规则，还是有时不遵守规则？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-97' id='a-97-1' value='1' data-am-ucheck><span class='lang'>总是遵守规则</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-97' id='a-97-2' value='2' data-am-ucheck><span class='lang'>不大遵守规则</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_98">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_98'></span>98. <span class='lang'>一个比你小的孩子没有经过你的允许拿你的东西玩，你是责备他，还是让他玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-98' id='a-98-1' value='1' data-am-ucheck><span class='lang'>责备他</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-98' id='a-98-2' value='2' data-am-ucheck><span class='lang'>让他玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_99">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_99'></span>99. <span class='lang'>当班里吵吵嚷嚷时，你仍能安静地学习，还是和大家一起吵嚷？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-99' id='a-99-1' value='1' data-am-ucheck><span class='lang'>安静地学习</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-99' id='a-99-2' value='2' data-am-ucheck><span class='lang'>和大家一起吵嚷</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_100">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_100'></span>100. <span class='lang'>你在大街上遇到熟人时，愿意主动跟他打招呼，还是有意避开？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-100' id='a-100-1' value='1' data-am-ucheck><span class='lang'>愿意主动打招呼</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-100' id='a-100-2' value='2' data-am-ucheck><span class='lang'>有意避开</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_101">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_101'></span>101. <span class='lang'>你经常受到老师的表扬，还是很少受到老师的表扬？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-101' id='a-101-1' value='1' data-am-ucheck><span class='lang'>经常受到表扬</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-101' id='a-101-2' value='2' data-am-ucheck><span class='lang'>很少受到表扬</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_102">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_102'></span>102. <span class='lang'>“走对跑”好比“慢对骑”还是“慢对快”、“慢对蜗牛”？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-102' id='a-102-1' value='1' data-am-ucheck><span class='lang'>慢对骑</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-102' id='a-102-2' value='2' data-am-ucheck><span class='lang'>慢对快</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-102' id='a-102-3' value='3' data-am-ucheck><span class='lang'>慢对蜗牛</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_103">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_103'></span>103. <span class='lang'>当你过一座窄桥时，你喜欢向桥下看，还是因桥又高又窄而发慌？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-103' id='a-103-1' value='1' data-am-ucheck><span class='lang'>喜欢向桥下看</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-103' id='a-103-2' value='2' data-am-ucheck><span class='lang'>发慌</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_104">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_104'></span>104. <span class='lang'>1、4、7下面一个数是9或10或8？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-104' id='a-104-1' value='1' data-am-ucheck><span class='lang'>是9</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-104' id='a-104-2' value='2' data-am-ucheck><span class='lang'>是10</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-104' id='a-104-3' value='3' data-am-ucheck><span class='lang'>是8</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_105">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_105'></span>105. <span class='lang'>你认为你长大了一定能干得不错，还是一般？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-105' id='a-105-1' value='1' data-am-ucheck><span class='lang'>干得不错</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-105' id='a-105-2' value='2' data-am-ucheck><span class='lang'>干得一般</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_106">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_106'></span>106. <span class='lang'>你对大人的话常常不服从，还是服从？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-106' id='a-106-1' value='1' data-am-ucheck><span class='lang'>不服从</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-106' id='a-106-2' value='2' data-am-ucheck><span class='lang'>服从</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_107">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_107'></span>107. <span class='lang'>你愿意当个法官，还是当个飞机驾驶员？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-107' id='a-107-1' value='1' data-am-ucheck><span class='lang'>当法官</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-107' id='a-107-2' value='2' data-am-ucheck><span class='lang'>当飞机驾驶员</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_108">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_108'></span>108. <span class='lang'>当你把借学校或者借同学的书弄坏了的时候，你常常就那样还回去，还是把它贴好再还？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-108' id='a-108-1' value='1' data-am-ucheck><span class='lang'>就那样还回去</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-108' id='a-108-2' value='2' data-am-ucheck><span class='lang'>贴好再还</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_109">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_109'></span>109. <span class='lang'>你愿意做你没有做过的工作，还是愿意做你熟悉的工作？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-109' id='a-109-1' value='1' data-am-ucheck><span class='lang'>没有做过的工作</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-109' id='a-109-2' value='2' data-am-ucheck><span class='lang'>熟悉的工作</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_110">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_110'></span>110. <span class='lang'>你很会讲笑话，还是觉得讲笑话是一件难事？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-110' id='a-110-1' value='1' data-am-ucheck><span class='lang'>会讲笑话</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-110' id='a-110-2' value='2' data-am-ucheck><span class='lang'>讲笑话是一件难事</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_111">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_111'></span>111. <span class='lang'>当你有了错误的时候，你很容易把它忘掉，还是总也忘不了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-111' id='a-111-1' value='1' data-am-ucheck><span class='lang'>很容易忘掉</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-111' id='a-111-2' value='2' data-am-ucheck><span class='lang'>总也忘不了</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_112">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_112'></span>112. <span class='lang'>放学后你喜欢玩，还是不大喜欢玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-112' id='a-112-1' value='1' data-am-ucheck><span class='lang'>喜欢玩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-112' id='a-112-2' value='2' data-am-ucheck><span class='lang'>不大喜欢玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_113">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_113'></span>113. <span class='lang'>放学后你喜欢和老师在一起，还是喜欢自己去玩？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-113' id='a-113-1' value='1' data-am-ucheck><span class='lang'>和老师在一起</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-113' id='a-113-2' value='2' data-am-ucheck><span class='lang'>喜欢自己去玩</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_114">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_114'></span>114. <span class='lang'>当你在外面惹了祸的时候，很害怕回家，还是只有一点点怕？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-114' id='a-114-1' value='1' data-am-ucheck><span class='lang'>很怕回家</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-114' id='a-114-2' value='2' data-am-ucheck><span class='lang'>只有一点点怕</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_115">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_115'></span>115. <span class='lang'>如果你是老师的话，你喜欢同学们有说有笑，还是安安静静的？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-115' id='a-115-1' value='1' data-am-ucheck><span class='lang'>有说有笑</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-115' id='a-115-2' value='2' data-am-ucheck><span class='lang'>安安静静的</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_116">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_116'></span>116. <span class='lang'>你的朗读比别人好，还是多数同学比你好？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-116' id='a-116-1' value='1' data-am-ucheck><span class='lang'>我比别人好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-116' id='a-116-2' value='2' data-am-ucheck><span class='lang'>多数同学比我好</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_117">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_117'></span>117. <span class='lang'>你是因为害怕老师和家长惩罚而学习，还是因为喜欢学习而努力学习？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-117' id='a-117-1' value='1' data-am-ucheck><span class='lang'>怕惩罚而学习</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-117' id='a-117-2' value='2' data-am-ucheck><span class='lang'>喜欢学习而努力学习</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_118">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_118'></span>118. <span class='lang'>当你生气的时候，总是不吱声，还是好发泄？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-118' id='a-118-1' value='1' data-am-ucheck><span class='lang'>不吱声</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-118' id='a-118-2' value='2' data-am-ucheck><span class='lang'>好发泄</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_119">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_119'></span>119. <span class='lang'>你喜欢自己的事情自己干，还是喜欢别人替你干？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-119' id='a-119-1' value='1' data-am-ucheck><span class='lang'>喜欢自己干</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-119' id='a-119-2' value='2' data-am-ucheck><span class='lang'>喜欢别人替我干</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_120">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_120'></span>120. <span class='lang'>你每天做作业和干家务活有固定的时间，还是什么时候想起就什么时候干？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-120' id='a-120-1' value='1' data-am-ucheck><span class='lang'>有固定的时间</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-120' id='a-120-2' value='2' data-am-ucheck><span class='lang'>什么时候想起就什么时候干</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_121">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_121'></span>121. <span class='lang'>你喜欢只有几个朋友，还是喜欢有很多朋友？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-121' id='a-121-1' value='1' data-am-ucheck><span class='lang'>只有几个朋友</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-121' id='a-121-2' value='2' data-am-ucheck><span class='lang'>喜欢有很多朋友</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_122">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_122'></span>122. <span class='lang'>在“全部”、“有些”、“经常”、“无”这些词中，哪一个词与其它词不一样？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-122' id='a-122-1' value='1' data-am-ucheck><span class='lang'>全部</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-122' id='a-122-2' value='2' data-am-ucheck><span class='lang'>无</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-122' id='a-122-3' value='3' data-am-ucheck><span class='lang'>经常</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_123">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_123'></span>123. <span class='lang'>你总是把事情干得很好，还是常常干不好？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-123' id='a-123-1' value='1' data-am-ucheck><span class='lang'>总是干得很好</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-123' id='a-123-2' value='2' data-am-ucheck><span class='lang'>常常干不好</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_124">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_124'></span>124. <span class='lang'>在小华像小萍现在那么大的时候，小薇比小华大，你说他们当中谁最小？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-124' id='a-124-1' value='1' data-am-ucheck><span class='lang'>小萍</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-124' id='a-124-2' value='2' data-am-ucheck><span class='lang'>小薇</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-124' id='a-124-3' value='3' data-am-ucheck><span class='lang'>小华</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_125">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_125'></span>125. <span class='lang'>你认为你的妈妈对你的帮助还很不够，还是过多了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-125' id='a-125-1' value='1' data-am-ucheck><span class='lang'>帮助不够</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-125' id='a-125-2' value='2' data-am-ucheck><span class='lang'>帮助过多</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_126">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_126'></span>126. <span class='lang'>当你做错了事大人笑话你的时候，你也笑，还是觉得很生气？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-126' id='a-126-1' value='1' data-am-ucheck><span class='lang'>我也笑</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-126' id='a-126-2' value='2' data-am-ucheck><span class='lang'>非常生气</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_127">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_127'></span>127. <span class='lang'>你见到客人时，总是先和客人说话，还是感到不好意思？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-127' id='a-127-1' value='1' data-am-ucheck><span class='lang'>和客人说话</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-127' id='a-127-2' value='2' data-am-ucheck><span class='lang'>不好意思</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_128">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_128'></span>128. <span class='lang'>坐在一间有说有笑的房间里学习，你认为是一件愉快的事，还是认为学习应该很安静？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-128' id='a-128-1' value='1' data-am-ucheck><span class='lang'>感到愉快</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-128' id='a-128-2' value='2' data-am-ucheck><span class='lang'>应当安静</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_129">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_129'></span>129. <span class='lang'>当你的父母接待客人时，你是走开，还是跟客人说话？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-129' id='a-129-1' value='1' data-am-ucheck><span class='lang'>走开</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-129' id='a-129-2' value='2' data-am-ucheck><span class='lang'>跟客人说话</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_130">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_130'></span>130. <span class='lang'>你认为大人不好交往，还是认为大多数大人是和蔼的？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-130' id='a-130-1' value='1' data-am-ucheck><span class='lang'>大人不好交往</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-130' id='a-130-2' value='2' data-am-ucheck><span class='lang'>大多数大人是和蔼的</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_131">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_131'></span>131. <span class='lang'>你是喜欢看有惊险场面的电影，还是有点害怕不大敢看？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-131' id='a-131-1' value='1' data-am-ucheck><span class='lang'>喜欢看</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-131' id='a-131-2' value='2' data-am-ucheck><span class='lang'>不大敢看</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_132">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_132'></span>132. <span class='lang'>比你小的孩子也敢取笑你，还是不敢取笑你？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-132' id='a-132-1' value='1' data-am-ucheck><span class='lang'>也敢取笑</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-132' id='a-132-2' value='2' data-am-ucheck><span class='lang'>不敢取笑</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_133">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_133'></span>133. <span class='lang'>当你跟朋友吵架之后，总觉得很恼火，还是不大在乎？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-133' id='a-133-1' value='1' data-am-ucheck><span class='lang'>觉得很恼火</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-133' id='a-133-2' value='2' data-am-ucheck><span class='lang'>不大在乎</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_134">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_134'></span>134. <span class='lang'>亲友们都认为你还像个小孩，还是认为你已像个大人了？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-134' id='a-134-1' value='1' data-am-ucheck><span class='lang'>像个小孩</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-134' id='a-134-2' value='2' data-am-ucheck><span class='lang'>像个大人</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_135">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_135'></span>135. <span class='lang'>你经常做你应该做的事情，还是做你愿意做的事情？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-135' id='a-135-1' value='1' data-am-ucheck><span class='lang'>做应该做的事情</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-135' id='a-135-2' value='2' data-am-ucheck><span class='lang'>做愿意做的事情</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_136">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_136'></span>136. <span class='lang'>你愿意学开飞机，还是愿意当一名警察？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-136' id='a-136-1' value='1' data-am-ucheck><span class='lang'>学开飞机</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-136' id='a-136-2' value='2' data-am-ucheck><span class='lang'>当警察</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_137">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_137'></span>137. <span class='lang'>你和同学们做游戏你输了的时候，总是埋怨别人没有配合好，还是不埋怨别人？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-137' id='a-137-1' value='1' data-am-ucheck><span class='lang'>好埋怨别人</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-137' id='a-137-2' value='2' data-am-ucheck><span class='lang'>不埋怨别人</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_138">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_138'></span>138. <span class='lang'>如果你把作业做错了，你是认为改不改都可以，还是认为必须把它改正过来？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-138' id='a-138-1' value='1' data-am-ucheck><span class='lang'>改不改都可以</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-138' id='a-138-2' value='2' data-am-ucheck><span class='lang'>必须把它改正过来</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_139">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_139'></span>139. <span class='lang'>如果你的朋友对你不好，你是原谅他，还是要报复他？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-139' id='a-139-1' value='1' data-am-ucheck><span class='lang'>原谅他</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-139' id='a-139-2' value='2' data-am-ucheck><span class='lang'>报复他</span></label></li></ul>
        </div>
      </div>
      
      <div class="q am-panel am-panel-default" id="q_140">
        <div class="am-panel-hd">
          <span class='tts am-btn am-btn-default am-btn-xs am-btn-hollow' data-target='#q_140'></span>140. <span class='lang'>你在班级中，经常认为自己有理而跟同学们争吵，还是愿意保持安静？</span>
        </div>
        <div class="q-answer am-panel-bd">
          <ul class='am-text-lg'><li><label class='am-radio am-danger'><input type='radio' name='a-140' id='a-140-1' value='1' data-am-ucheck><span class='lang'>认为有理而争吵</span></label></li><li><label class='am-radio am-danger'><input type='radio' name='a-140' id='a-140-2' value='2' data-am-ucheck><span class='lang'>愿意保持安静</span></label></li></ul>
        </div>
      </div>
      
    </form>
    <div class="q-act">
      <input type="button" class="am-btn am-btn-success am-btn-sm btn-prev" value="上一题">
      <input type="button" class="am-btn am-btn-success am-btn-sm btn-next" value="下一题">
      <select id="select" data-am-selected="{btnWidth:'55px',btnSize:'xs',btnStyle:'success',dropUp:1,maxHeight:'350px',searchBox:1}">
        
        <option value="1">1</option>
        
        <option value="2">2</option>
        
        <option value="3">3</option>
        
        <option value="4">4</option>
        
        <option value="5">5</option>
        
        <option value="6">6</option>
        
        <option value="7">7</option>
        
        <option value="8">8</option>
        
        <option value="9">9</option>
        
        <option value="10">10</option>
        
        <option value="11">11</option>
        
        <option value="12">12</option>
        
        <option value="13">13</option>
        
        <option value="14">14</option>
        
        <option value="15">15</option>
        
        <option value="16">16</option>
        
        <option value="17">17</option>
        
        <option value="18">18</option>
        
        <option value="19">19</option>
        
        <option value="20">20</option>
        
        <option value="21">21</option>
        
        <option value="22">22</option>
        
        <option value="23">23</option>
        
        <option value="24">24</option>
        
        <option value="25">25</option>
        
        <option value="26">26</option>
        
        <option value="27">27</option>
        
        <option value="28">28</option>
        
        <option value="29">29</option>
        
        <option value="30">30</option>
        
        <option value="31">31</option>
        
        <option value="32">32</option>
        
        <option value="33">33</option>
        
        <option value="34">34</option>
        
        <option value="35">35</option>
        
        <option value="36">36</option>
        
        <option value="37">37</option>
        
        <option value="38">38</option>
        
        <option value="39">39</option>
        
        <option value="40">40</option>
        
        <option value="41">41</option>
        
        <option value="42">42</option>
        
        <option value="43">43</option>
        
        <option value="44">44</option>
        
        <option value="45">45</option>
        
        <option value="46">46</option>
        
        <option value="47">47</option>
        
        <option value="48">48</option>
        
        <option value="49">49</option>
        
        <option value="50">50</option>
        
        <option value="51">51</option>
        
        <option value="52">52</option>
        
        <option value="53">53</option>
        
        <option value="54">54</option>
        
        <option value="55">55</option>
        
        <option value="56">56</option>
        
        <option value="57">57</option>
        
        <option value="58">58</option>
        
        <option value="59">59</option>
        
        <option value="60">60</option>
        
        <option value="61">61</option>
        
        <option value="62">62</option>
        
        <option value="63">63</option>
        
        <option value="64">64</option>
        
        <option value="65">65</option>
        
        <option value="66">66</option>
        
        <option value="67">67</option>
        
        <option value="68">68</option>
        
        <option value="69">69</option>
        
        <option value="70">70</option>
        
        <option value="71">71</option>
        
        <option value="72">72</option>
        
        <option value="73">73</option>
        
        <option value="74">74</option>
        
        <option value="75">75</option>
        
        <option value="76">76</option>
        
        <option value="77">77</option>
        
        <option value="78">78</option>
        
        <option value="79">79</option>
        
        <option value="80">80</option>
        
        <option value="81">81</option>
        
        <option value="82">82</option>
        
        <option value="83">83</option>
        
        <option value="84">84</option>
        
        <option value="85">85</option>
        
        <option value="86">86</option>
        
        <option value="87">87</option>
        
        <option value="88">88</option>
        
        <option value="89">89</option>
        
        <option value="90">90</option>
        
        <option value="91">91</option>
        
        <option value="92">92</option>
        
        <option value="93">93</option>
        
        <option value="94">94</option>
        
        <option value="95">95</option>
        
        <option value="96">96</option>
        
        <option value="97">97</option>
        
        <option value="98">98</option>
        
        <option value="99">99</option>
        
        <option value="100">100</option>
        
        <option value="101">101</option>
        
        <option value="102">102</option>
        
        <option value="103">103</option>
        
        <option value="104">104</option>
        
        <option value="105">105</option>
        
        <option value="106">106</option>
        
        <option value="107">107</option>
        
        <option value="108">108</option>
        
        <option value="109">109</option>
        
        <option value="110">110</option>
        
        <option value="111">111</option>
        
        <option value="112">112</option>
        
        <option value="113">113</option>
        
        <option value="114">114</option>
        
        <option value="115">115</option>
        
        <option value="116">116</option>
        
        <option value="117">117</option>
        
        <option value="118">118</option>
        
        <option value="119">119</option>
        
        <option value="120">120</option>
        
        <option value="121">121</option>
        
        <option value="122">122</option>
        
        <option value="123">123</option>
        
        <option value="124">124</option>
        
        <option value="125">125</option>
        
        <option value="126">126</option>
        
        <option value="127">127</option>
        
        <option value="128">128</option>
        
        <option value="129">129</option>
        
        <option value="130">130</option>
        
        <option value="131">131</option>
        
        <option value="132">132</option>
        
        <option value="133">133</option>
        
        <option value="134">134</option>
        
        <option value="135">135</option>
        
        <option value="136">136</option>
        
        <option value="137">137</option>
        
        <option value="138">138</option>
        
        <option value="139">139</option>
        
        <option value="140">140</option>
        
      </select>
    </div>
  </article>
</div>
<div class="am-modal am-modal-alert" id="alert">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-break"></div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-alert" id="alert-notcheck">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-break">第 <span></span> 题未选答案。</div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-alert" id="alert-toofast">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-break">你的测评用时较短，请重新测评。</div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-alert" id="alert-tooslow">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-break">本量表限时为 <span></span> 分钟，现在时间已到。</div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-alert" id="alert-lie">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-break">你在回答问题过程中有掩盖自己本身真实想法的行为，因此测量的结果有可能不符合你的实际情况，请你在适当的时间重新测评。</div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-confirm" id="confirm">
  <div class="am-modal-dialog">
    <div class="am-modal-bd"></div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-default am-btn-hollow" data-am-modal-cancel>取消</button>
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>确定</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-confirm" id="confirm-garlic">
  <div class="am-modal-dialog">
    <div class="am-modal-hd">系统提示</div>
    <div class="am-modal-bd">系统检测到该设备上有未完成的测评。<br>如果不是你本人作答，请选重新开始；<br>如果是你本人作答，但中途退出过，可选重新开始或继续作答（保留原有答题选项）。</div>
    <div class="am-modal-footer">
      <button type="button" class="am-btn am-modal-btn am-btn-default am-btn-hollow" data-am-modal-cancel>继续作答</button>
      <button type="button" class="am-btn am-modal-btn am-btn-primary" data-am-modal-confirm>重新开始</button>
    </div>
  </div>
</div>
<div class="am-modal am-modal-loading am-modal-no-btn" id="loading">
  <div class="am-modal-dialog">
    <div class="am-modal-bd am-text-center">
      <i class="am-icon-spinner am-icon-spin"></i>
      <p style="padding-left:0;">正在载入...</p>
    </div>
  </div>
</div>
<script src="//cdn.bootcdn.net/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="//cdn.bootcdn.net/ajax/libs/garlic.js/1.4.2/garlic.min.js"></script>
<script src="//cdn.bootcdn.net/ajax/libs/autosize.js/4.0.4/autosize.min.js"></script>
<script src="//cdn.bootcdn.net/ajax/libs/store2/2.14.2/store2.min.js"></script>
<script src="//cdn.bootcdn.net/ajax/libs/blueimp-md5/2.19.0/js/md5.min.js"></script>
<script src="//res.wx.qq.com/open/js/jweixin-1.6.0.js"></script>
<script src="//cdn.psy.com.cn/scripts/amazeui/js/amazeui.min.js"></script>
<script src="/lb/inc/test-obfuscated.js"></script>

</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmla)
qid = 0
divs = soup.select('div.q.am-panel.am-panel-default')
total= 0
# 打印匹配结果
for div in divs:
    qid +=1
    print("-------\n")
    sdiv = soup.find('div', id='q_' + str(qid))
    if sdiv!=None:
        total += 1
        # print(sdiv)
        lis = sdiv.select('div.am-panel-hd > span')
        print('q_' + str(qid)+':')
        for li in lis:
            print(li.text.strip())  # 输出每个li标签的文本内容（去除首尾空格）
        print("\n")
        # 或者使用 select() 方法直接访问下级标签内容
        lis = sdiv.select('div.q-answer > ul > li')
        print("答案选项为")
        answer = 0
        # 遍历所有的li标签，获取里面的文本内容
        for li in lis:
            answer +=1
            print(str(answer)+'.'+li.text.strip())  # 输出每个li标签的文本内容（去除首尾空格）
        print("\n")